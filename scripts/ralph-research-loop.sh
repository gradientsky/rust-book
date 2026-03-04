#!/usr/bin/env bash
# Run the research Ralph loop
# Usage: ./scripts/ralph-research-loop.sh [--project DIR] [iterations]
#   --project DIR  Run research in a subdirectory (e.g. conway-game)
#   Default: 5 iterations, no project subdirectory

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

PROJECT_ARGS=()
ITERATIONS=5

while [[ $# -gt 0 ]]; do
    case $1 in
        --project) PROJECT_ARGS=(--project-dir "$2"); shift 2 ;;
        *)         ITERATIONS="$1"; shift ;;
    esac
done

# Signal handling is delegated to claude-code.sh.
# Ctrl-C reaches both this shell and claude-code.sh (same foreground group);
# claude-code.sh's trap handles cleanup, then this shell exits via set -e.
"$SCRIPT_DIR/claude-code.sh" --name RESEARCH_LOOP_PROMPT.md --max-iter "$ITERATIONS" "${PROJECT_ARGS[@]}"
