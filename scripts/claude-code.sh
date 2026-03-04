#!/usr/bin/env bash
# Run Claude Code non-interactively with visualized output
# Usage: ./scripts/claude-code.sh --name prompt.txt
#        ./scripts/claude-code.sh --name prompt.txt --max-iter 5
#        ./scripts/claude-code.sh --name prompt.txt --max-iter 0  # infinite

set -eo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# --- Signal handling ---------------------------------------------------
#
# Claude runs in its own session (setsid) writing to a FIFO.
# The visualizer reads from the FIFO in the background.
#
# This architecture solves three problems:
#
#   1. Bash defers trap handlers until a foreground command completes,
#      and Claude Code catches SIGINT internally without exiting.
#      A foreground pipeline would swallow Ctrl-C entirely.
#
#   2. With setsid, Claude is in a separate process group.
#      Ctrl-C (SIGINT) reaches only this script, not Claude.
#      The trap handler fires immediately and explicitly terminates
#      Claude's group — no racing with Claude's signal handling.
#
#   3. If Claude's bash tool starts a background process (e.g., a dev
#      server for verification), that process inherits Claude's stdout.
#      With a pipe, the orphaned process keeps the pipe open, python
#      never gets EOF, and wait blocks forever. With a FIFO, we wait
#      for Claude alone, then kill the process group (closing all FIFO
#      writers), and python gets EOF naturally.

iter=0
CLAUDE_PGID=""
VIZ_PID=""
FIFO=""

cleanup() {
    trap '' INT TERM HUP                            # ignore signals during cleanup
    echo "" >&2
    echo "━━━ Interrupted after $iter iteration(s) ━━━" >&2
    if [[ -n "$CLAUDE_PGID" ]]; then
        kill -- -"$CLAUDE_PGID" 2>/dev/null || true # TERM to Claude's group
        sleep 0.5                                    # grace period
        kill -9 -- -"$CLAUDE_PGID" 2>/dev/null || true # KILL survivors
    fi
    if [[ -n "$VIZ_PID" ]]; then
        kill "$VIZ_PID" 2>/dev/null || true
    fi
    [[ -n "$FIFO" ]] && rm -f "$FIFO"
    wait 2>/dev/null || true                         # reap
    exit 130
}
trap cleanup INT TERM HUP

# --- Argument parsing --------------------------------------------------

MAX_ITER=1
PROMPT_FILE=""
PROJECT_DIR=""
while [[ $# -gt 0 ]]; do
    case $1 in
        --max-iter)    MAX_ITER="$2"; shift 2 ;;
        --name)        PROMPT_FILE="$2"; shift 2 ;;
        --project-dir) PROJECT_DIR="$2"; shift 2 ;;
        *)
            echo "Unknown option: $1" >&2
            echo "Usage: $0 --name <file> [--max-iter N] [--project-dir DIR]" >&2
            exit 1
            ;;
    esac
done

if [[ -z "$PROMPT_FILE" ]]; then
    echo "Error: --name <file> is required" >&2
    echo "Usage: $0 --name <file> [--max-iter N] [--project-dir DIR]" >&2
    exit 1
fi

if [[ ! -f "$PROMPT_FILE" ]]; then
    echo "Error: File not found: $PROMPT_FILE" >&2
    exit 1
fi

if [[ -n "$PROJECT_DIR" && ! -d "$PROJECT_DIR" ]]; then
    echo "Error: Project directory not found: $PROJECT_DIR" >&2
    exit 1
fi

# --- Main loop ---------------------------------------------------------

while [[ $MAX_ITER -eq 0 ]] || [[ $iter -lt $MAX_ITER ]]; do
    ((iter++)) || true

    if [[ $MAX_ITER -eq 0 ]]; then
        echo "━━━ Iteration $iter (infinite mode) ━━━" >&2
    else
        echo "━━━ Iteration $iter/$MAX_ITER ━━━" >&2
    fi

    PROMPT="$(cat "$PROMPT_FILE")"

    # If a project directory is specified, resolve its absolute path and
    # instruct Claude to use it for ALL file operations. Claude resolves
    # relative paths from the git root, not from cwd, so we must provide
    # the absolute project path and tell the agent to prefix everything.
    if [[ -n "$PROJECT_DIR" ]]; then
        PROJECT_DIR_ABS="$(cd "$PROJECT_DIR" && pwd)"
        WORKSPACE_ROOT="$(pwd)"
        PROJECT_PREFIX="The project lives under ${PROJECT_DIR_ABS}/.
IMPORTANT: All file operations must use paths under ${PROJECT_DIR_ABS}/.
When task specs or documents reference relative paths (src/engine/types.ts, plan.md, tasks/implementation/FND-0001.md, etc.), always prefix them with ${PROJECT_DIR_ABS}/.
When running shell commands (npm, npx, vitest, tsc), cd to ${PROJECT_DIR_ABS}/ first.
.claude/ paths are at ${WORKSPACE_ROOT}/.claude/.

"
        PROMPT="${PROJECT_PREFIX}${PROMPT}"
    fi

    echo -e "\033[97m┌─ Prompt ($iter/$MAX_ITER):\033[0m" >&2
    echo "$PROMPT" | sed 's/^/│ /' | while read -r line; do
        echo -e "\033[97m$line\033[0m"
    done >&2
    echo -e "\033[97m└─\033[0m" >&2
    echo "" >&2

    # --- FIFO-based pipeline ----------------------------------------------
    #
    # Claude writes to a FIFO; the visualizer reads from it.
    # This decouples the two processes so we can:
    #   1. Wait for Claude to finish (bash -c exits when claude exits)
    #   2. Kill orphaned children in Claude's setsid group
    #   3. Let the visualizer finish naturally (gets EOF when all writers die)
    #
    # With a direct pipe (claude | python), orphaned children of Claude
    # that inherit the pipe fd prevent python from ever getting EOF.

    FIFO=$(mktemp -u /tmp/claude-pipe.XXXXXX)
    mkfifo "$FIFO"

    # Start visualizer reading from FIFO (streams output in real-time)
    python3 -u "${SCRIPT_DIR}/visualize.py" < "$FIFO" &
    VIZ_PID=$!

    # Run Claude in its own session, writing to FIFO.
    # $1=prompt, $2=FIFO path, $3=project dir (empty string if none).
    # If a project dir is specified, cd into it so all relative paths resolve naturally.
    #
    # setsid is Linux-only; on macOS, use Perl's POSIX::setsid to create a
    # new session so Ctrl-C doesn't reach Claude directly.
    # stdbuf is GNU coreutils; skip it if unavailable (macOS).
    _STDBUF=""
    command -v stdbuf &>/dev/null && _STDBUF="stdbuf -oL"

    if command -v setsid &>/dev/null; then
        setsid bash -c '
            [[ -n "$4" ]] && cd "$4"
            $3 claude -p --dangerously-skip-permissions \
                --output-format=stream-json --model opus --verbose "$1" > "$2"' \
            _ "$PROMPT" "$FIFO" "$_STDBUF" "${PROJECT_DIR_ABS:-}" &
    else
        # macOS: use Perl POSIX::setsid to create a new session, then exec bash
        perl -e 'use POSIX "setsid"; setsid() or die "setsid: $!"; exec @ARGV' \
            bash -c '
            [[ -n "$4" ]] && cd "$4"
            $3 claude -p --dangerously-skip-permissions \
                --output-format=stream-json --model opus --verbose "$1" > "$2"' \
            _ "$PROMPT" "$FIFO" "$_STDBUF" "${PROJECT_DIR_ABS:-}" &
    fi
    CLAUDE_PGID=$!

    # Wait for Claude to finish (bash -c exits when claude exits)
    wait $CLAUDE_PGID || true

    # Kill orphaned children in Claude's session (e.g., dev servers started
    # by verification commands). This closes their FIFO fd handles.
    kill -- -"$CLAUDE_PGID" 2>/dev/null || true
    sleep 0.3
    kill -9 -- -"$CLAUDE_PGID" 2>/dev/null || true

    # All FIFO writers are now dead — visualizer gets EOF and exits
    wait $VIZ_PID || true

    rm -f "$FIFO"
    CLAUDE_PGID=""
    VIZ_PID=""
    FIFO=""
done

echo "" >&2
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━" >&2
echo "✓ Completed $iter iteration(s)" >&2
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━" >&2
