#!/usr/bin/env python3
"""
Visualize Claude Code JSONL output in a terminal-friendly format.

Usage:
    cat output.txt | python scripts/visualize.py
    python scripts/visualize.py < output.txt
    python scripts/visualize.py output.txt
"""

import json
import sys
import re
import difflib
import subprocess
import shutil

# Check if glow is available
GLOW_AVAILABLE = shutil.which("glow") is not None


def render_markdown(text: str, indent: str = "   ") -> None:
    """Render markdown using glow if available, otherwise basic formatting."""
    if GLOW_AVAILABLE:
        try:
            result = subprocess.run(
                ["glow", "-s", "dark", "-w", "100"],
                input=text,
                capture_output=True,
                text=True,
                timeout=5
            )
            if result.returncode == 0:
                for line in result.stdout.split("\n"):
                    print(f"{indent}{line}")
                return
        except (subprocess.TimeoutExpired, Exception):
            pass

    # Fallback: basic markdown rendering
    for line in text.split("\n"):
        if line.startswith("# "):
            print(colorize(f"{indent}{line}", Colors.BOLD, Colors.WHITE))
        elif line.startswith("## "):
            print(colorize(f"{indent}{line}", Colors.BOLD, Colors.CYAN))
        elif line.startswith("### "):
            print(colorize(f"{indent}{line}", Colors.BOLD, Colors.YELLOW))
        elif line.startswith("#### "):
            print(colorize(f"{indent}{line}", Colors.BOLD, Colors.MAGENTA))
        elif line.startswith("- ") or line.startswith("* "):
            print(apply_inline_emphasis(f"{indent}{line}"))
        elif line.startswith("```"):
            print(colorize(f"{indent}{line}", Colors.DIM))
        elif line.startswith("|"):
            print(colorize(f"{indent}{line}", Colors.CYAN))
        elif line.startswith("> "):
            print(colorize(f"{indent}{line}", Colors.DIM, Colors.ITALIC))
        # Beads-specific formatting
        elif line.startswith("○ "):
            # Open issue
            print(colorize(f"{indent}{line}", Colors.CYAN))
        elif line.startswith("● "):
            # Closed/active issue
            print(colorize(f"{indent}{line}", Colors.GREEN))
        elif line.strip().startswith("[●") or line.strip().startswith("[○"):
            # Issue status tags
            print(colorize(f"{indent}{line}", Colors.YELLOW))
        elif "DESCRIPTION" in line or "DEPENDENCIES" in line or "COMMENTS" in line:
            # Beads section headers
            print(colorize(f"{indent}{line}", Colors.BOLD, Colors.WHITE))
        else:
            print(apply_inline_emphasis(f"{indent}{line}"))

# ANSI color codes
class Colors:
    RESET = "\033[0m"
    BOLD = "\033[1m"
    DIM = "\033[2m"
    ITALIC = "\033[3m"

    # Foreground
    BLACK = "\033[30m"
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    MAGENTA = "\033[35m"
    CYAN = "\033[36m"
    WHITE = "\033[37m"

    # Bright foreground
    BRIGHT_BLACK = "\033[90m"
    BRIGHT_RED = "\033[91m"
    BRIGHT_GREEN = "\033[92m"
    BRIGHT_YELLOW = "\033[93m"
    BRIGHT_BLUE = "\033[94m"
    BRIGHT_MAGENTA = "\033[95m"
    BRIGHT_CYAN = "\033[96m"
    BRIGHT_WHITE = "\033[97m"


def colorize(text: str, *codes: str) -> str:
    """Apply ANSI color codes to text."""
    return "".join(codes) + text + Colors.RESET


def apply_inline_emphasis(line: str) -> str:
    """Replace **bold** and __bold__ with ANSI bold."""
    bold, reset = Colors.BOLD, Colors.RESET
    line = re.sub(r'\*\*(.+?)\*\*', lambda m: f'{bold}{m.group(1)}{reset}', line)
    line = re.sub(r'__(.+?)__', lambda m: f'{bold}{m.group(1)}{reset}', line)
    return line



def render_system_message(msg: dict) -> None:
    """Render system messages (init, hook_response)."""
    subtype = msg.get("subtype", "")

    if subtype == "init":
        print(colorize("━" * 60, Colors.DIM))
        print(colorize("SESSION INITIALIZED", Colors.BOLD, Colors.CYAN))
        print(colorize(f"  Model: {msg.get('model', 'unknown')}", Colors.DIM))
        print(colorize(f"  CWD: {msg.get('cwd', 'unknown')}", Colors.DIM))
        tools = msg.get("tools", [])
        if tools:
            print(colorize(f"  Tools: {', '.join(tools)}", Colors.DIM))
        print(colorize("━" * 60, Colors.DIM))
        print()

    elif subtype == "hook_response":
        hook_name = msg.get("hook_name", "unknown")
        stdout = msg.get("stdout", "")
        print(colorize(f"⚡ Hook: {hook_name}", Colors.YELLOW))
        if stdout:
            # Hook output is often markdown (e.g., beads workflow)
            render_markdown(stdout.strip())
        print()


def classify_tool(name: str, input_data: dict) -> str:
    """Classify a tool by normalized name or input shape.

    Returns a canonical key used for icon lookup and rendering dispatch.
    This avoids brittleness from exact tool name matching — Claude Code
    tool names change across versions (e.g. AgentOutput → TaskOutputTool → TaskOutput).
    """
    lower = name.lower().replace("tool", "")

    # Spawn sub-agent
    if lower == "task" and "subagent_type" in input_data:
        return "Task"
    # Check sub-agent output (covers TaskOutput, TaskOutputTool, AgentOutput, etc.)
    if "task_id" in input_data and ("block" in input_data or "timeout" in input_data):
        return "TaskOutput"
    # Task management tools
    if "subject" in input_data and "description" in input_data and lower.startswith("task"):
        return "TaskCreate"
    if "taskId" in input_data and "status" in input_data:
        return "TaskUpdate"
    if "taskId" in input_data and "status" not in input_data:
        return "TaskGet"
    if lower in ("tasklist",):
        return "TaskList"

    # Exact-match the rest (stable tool names) → canonical form
    CANONICAL = {
        "read": "Read", "write": "Write", "edit": "Edit",
        "bash": "Bash", "glob": "Glob", "grep": "Grep",
        "skill": "Skill", "todowrite": "TodoWrite",
        "webfetch": "WebFetch", "websearch": "WebSearch",
        "askuserquestion": "AskUserQuestion",
    }
    canonical = CANONICAL.get(lower)
    if canonical:
        return canonical
    return name


# Tool icons — keyed by canonical name from classify_tool()
TOOL_ICONS = {
    "Read": "📖",
    "Write": "✏️",
    "Edit": "📝",
    "Bash": "💻",
    "Glob": "🔍",
    "Grep": "🔎",
    "Task": "🤖",
    "TaskOutput": "📡",
    "TaskCreate": "📋",
    "TaskUpdate": "📋",
    "TaskList": "📋",
    "TaskGet": "📋",
    "TodoWrite": "📋",
    "WebFetch": "🌐",
    "WebSearch": "🔍",
    "Skill": "⚡",
    "AskUserQuestion": "❓",
}


def render_tool_use(tool: dict) -> None:
    """Render a tool_use block."""
    name = tool.get("name", "unknown")
    input_data = tool.get("input", {})
    kind = classify_tool(name, input_data)
    icon = TOOL_ICONS.get(kind, "🔧")

    print(colorize(f"{icon} {name}", Colors.BOLD, Colors.MAGENTA), end="")

    # Show relevant input parameters
    if kind == "Read":
        path = input_data.get("file_path", "")
        print(colorize(f" {path}", Colors.CYAN))
    elif kind == "Write":
        path = input_data.get("file_path", "")
        content = input_data.get("content", "")
        num_lines = content.count("\n") + 1 if content else 0
        num_bytes = len(content.encode("utf-8")) if content else 0
        print(colorize(f" {path}", Colors.CYAN), end="")
        print(colorize(f" ({num_lines} lines, {format_bytes(num_bytes)})", Colors.DIM))
    elif kind == "Edit":
        path = input_data.get("file_path", "")
        print(colorize(f" {path}", Colors.CYAN))
        old_string = input_data.get("old_string", "")
        new_string = input_data.get("new_string", "")
        if old_string or new_string:
            # Generate unified diff
            old_lines = old_string.splitlines(keepends=True)
            new_lines = new_string.splitlines(keepends=True)
            diff = difflib.unified_diff(old_lines, new_lines, lineterm="")

            print(colorize("   ┌─ Diff:", Colors.YELLOW))
            for line in diff:
                line = line.rstrip("\n")
                if line in ("---", "+++") or re.match(r'^@@ .+ @@', line):
                    continue
                elif line.startswith("+"):
                    print(colorize(f"   │ {line}", Colors.GREEN))
                elif line.startswith("-"):
                    print(colorize(f"   │ {line}", Colors.RED))
                else:
                    print(colorize(f"   │ {line}", Colors.DIM))
            print(colorize("   └─", Colors.YELLOW))
    elif kind == "Bash":
        cmd = input_data.get("command", "")
        desc = input_data.get("description", "")
        if desc:
            print(colorize(f" {desc}", Colors.DIM))
        else:
            print(colorize(f" {cmd}", Colors.DIM))
    elif kind == "Glob":
        pattern = input_data.get("pattern", "")
        print(colorize(f" {pattern}", Colors.CYAN))
    elif kind == "Grep":
        pattern = input_data.get("pattern", "")
        print(colorize(f" /{pattern}/", Colors.CYAN))
    elif kind == "Task":
        desc = input_data.get("description", "")
        agent = input_data.get("subagent_type", "")
        print(colorize(f" [{agent}] {desc}", Colors.CYAN))
    elif kind == "Skill":
        skill = input_data.get("skill", "")
        print(colorize(f" /{skill}", Colors.CYAN))
    elif kind == "TaskOutput":
        task_id = input_data.get("task_id", "")
        block = input_data.get("block", True)
        mode = "blocking" if block else "non-blocking"
        print(colorize(f" {task_id}", Colors.CYAN), end="")
        print(colorize(f" ({mode})", Colors.DIM))
    elif kind == "TaskCreate":
        subject = input_data.get("subject", "")
        print(colorize(f" {subject}", Colors.CYAN))
    elif kind == "TaskUpdate":
        task_id = input_data.get("taskId", "")
        status = input_data.get("status", "")
        print(colorize(f" {task_id}", Colors.CYAN), end="")
        if status:
            print(colorize(f" → {status}", Colors.YELLOW))
        else:
            print()
    elif kind == "TaskList":
        print()
    elif kind == "TaskGet":
        task_id = input_data.get("taskId", "")
        print(colorize(f" {task_id}", Colors.CYAN))
    elif kind == "WebSearch":
        query = input_data.get("query", "")
        print(colorize(f" q=\"{query}\"", Colors.CYAN))
    elif kind == "WebFetch":
        url = input_data.get("url", "")
        print(colorize(f" {url}", Colors.CYAN))
    elif kind == "TodoWrite":
        todos = input_data.get("todos", [])
        print(colorize(f" ({len(todos)} items)", Colors.DIM))
        for todo in todos:
            status = todo.get("status", "pending")
            content = todo.get("content", todo.get("subject", ""))
            if status == "completed":
                icon, color = "✓", Colors.GREEN
            elif status == "in_progress":
                icon, color = "▶", Colors.YELLOW
            else:
                icon, color = "○", Colors.DIM
            print(colorize(f"   {icon} {content}", color))
    else:
        # Generic: show first key-value
        if input_data:
            first_key = list(input_data.keys())[0]
            first_val = str(input_data[first_key])[:50]
            print(colorize(f" {first_key}={first_val}", Colors.DIM))
        else:
            print()


def format_duration(ms: float) -> str:
    """Format milliseconds as human-readable duration (e.g. 1h 23min 14s)."""
    total_secs = int(ms / 1000)
    hours, remainder = divmod(total_secs, 3600)
    minutes, seconds = divmod(remainder, 60)

    parts = []
    if hours:
        parts.append(f"{hours}h")
    if minutes:
        parts.append(f"{minutes}min")
    if seconds or not parts:
        parts.append(f"{seconds}s")
    return " ".join(parts)


def format_bytes(num_bytes: int) -> str:
    """Format bytes in human-readable format."""
    for unit in ["B", "KB", "MB", "GB"]:
        if abs(num_bytes) < 1024:
            return f"{num_bytes:.1f}{unit}" if unit != "B" else f"{num_bytes}{unit}"
        num_bytes /= 1024
    return f"{num_bytes:.1f}TB"


def _parse_subagent_metadata(text: str) -> tuple[str, dict, str]:
    """Extract agentId, usage stats, and clean body from subagent result text."""
    body = text or ""
    agent_id = ""
    usage_stats: dict[str, str] = {}

    agent_match = re.search(r"agentId:\s*(\S+)", body)
    if agent_match:
        agent_id = agent_match.group(1)

    usage_match = re.search(r"<usage>(.*?)</usage>", body, re.DOTALL)
    if usage_match:
        for kv in re.findall(r"(\w+):\s*([\d.]+)", usage_match.group(1)):
            usage_stats[kv[0]] = kv[1]

    # Strip metadata from body
    body = re.sub(r"agentId:.*(\n|$)", "", body)
    body = re.sub(r"<usage>.*?</usage>", "", body, flags=re.DOTALL)
    body = body.rstrip()

    return agent_id, usage_stats, body


def _format_usage_summary(agent_id: str, usage_stats: dict) -> str:
    """Format agent metadata into a compact one-liner."""
    parts = []
    if agent_id:
        parts.append(f"agent:{agent_id}")
    tokens = usage_stats.get("total_tokens")
    if tokens:
        parts.append(f"{int(tokens):,} tokens")
    tools = usage_stats.get("tool_uses")
    if tools:
        parts.append(f"{tools} tool calls")
    duration = usage_stats.get("duration_ms")
    if duration:
        parts.append(format_duration(float(duration)))
    return " · ".join(parts)


def _extract_jsonl_summary(content_text: str) -> tuple[str, str, int, int]:
    """Extract a readable summary from raw JSONL task output.

    Returns (final_text, output_file, num_tool_calls, num_messages).
    """
    lines = content_text.strip().split("\n")
    final_text = ""
    output_file = ""
    num_tool_calls = 0
    num_messages = 0

    # Check for output file path in truncation marker
    trunc_match = re.search(r'\[Truncated\. Full output: ([^\]]+)\]', content_text)
    if trunc_match:
        output_file = trunc_match.group(1).strip()

    for raw_line in lines:
        raw_line = raw_line.strip()
        if not raw_line or not raw_line.startswith("{"):
            continue
        try:
            msg = json.loads(raw_line)
        except json.JSONDecodeError:
            continue

        msg_type = msg.get("type", "")

        if msg_type == "assistant":
            num_messages += 1
            for block in msg.get("message", {}).get("content", []):
                if block.get("type") == "text":
                    text = block.get("text", "").strip()
                    if text:
                        final_text = text
                elif block.get("type") == "tool_use":
                    num_tool_calls += 1

    return final_text, output_file, num_tool_calls, num_messages


def _is_jsonl(text: str) -> bool:
    """Check if text looks like JSONL (multiple JSON lines)."""
    lines = text.strip().split("\n")
    json_lines = 0
    for line in lines[:5]:  # Check first 5 non-empty lines
        line = line.strip()
        if line and line.startswith("{"):
            try:
                json.loads(line)
                json_lines += 1
            except json.JSONDecodeError:
                pass
    return json_lines >= 2


def _parse_task_output_wrapper(text: str) -> dict | None:
    """Parse XML-tagged TaskOutput wrapper (timeout, running status, etc.).

    Returns dict with extracted fields if detected, None otherwise.
    """
    if not text or "<retrieval_status>" not in text:
        return None

    result = {}
    for tag in ("retrieval_status", "task_id", "task_type", "status"):
        match = re.search(rf'<{tag}>(.*?)</{tag}>', text, re.DOTALL)
        if match:
            result[tag] = match.group(1).strip()

    # Output file from truncation marker
    trunc_match = re.search(r'\[Truncated\. Full output: ([^\]]+)\]', text)
    if trunc_match:
        result["output_file"] = trunc_match.group(1).strip()

    # Embedded JSONL after <output> tag
    output_match = re.search(r'<output>\s*(.*)', text, re.DOTALL)
    if output_match:
        result["raw_output"] = output_match.group(1).strip()

    return result if result else None


def render_subagent_result(tool_input: dict, content_text: str, is_error: bool) -> None:
    """Render a sub-agent (Task/TaskOutput) result with distinct visual treatment."""
    agent_type = tool_input.get("subagent_type", "")
    description = tool_input.get("description", "")
    task_id = tool_input.get("task_id", "")

    # Build header label
    if agent_type and description:
        label = f"{agent_type} — {description}"
    elif agent_type:
        label = agent_type
    elif description:
        label = description
    elif task_id:
        label = f"task {task_id}"
    else:
        label = "sub-agent"

    agent_id, usage_stats, body = _parse_subagent_metadata(content_text)

    # Async launch boilerplate — collapse to one line
    if "launched successfully" in (content_text or "") or "working in the background" in (content_text or ""):
        summary = _format_usage_summary(agent_id, usage_stats)
        line = f"   ↳ launched in background"
        if summary:
            line += f"  ({summary})"
        print(colorize(line, Colors.DIM))
        return

    # XML-wrapped TaskOutput (timeout/running with embedded transcript)
    footer_lines: list[str] = []
    wrapper = _parse_task_output_wrapper(content_text or "")
    if wrapper:
        retrieval_status = wrapper.get("retrieval_status", "")
        status = wrapper.get("status", "")
        output_file = wrapper.get("output_file", "")

        # Status indicator
        if retrieval_status == "timeout":
            status_msg = f"timed out (agent still {status})" if status else "timed out"
        elif status:
            status_msg = status
        else:
            status_msg = retrieval_status
        footer_lines.append(f"⏳ {status_msg}")

        # Extract final text from embedded JSONL
        raw_output = wrapper.get("raw_output", "")
        if raw_output and _is_jsonl(raw_output):
            final_text, of2, num_tool_calls, num_messages = _extract_jsonl_summary(raw_output)
            body = final_text
            output_file = output_file or of2
            stats = []
            if num_messages:
                stats.append(f"{num_messages} turns")
            if num_tool_calls:
                stats.append(f"{num_tool_calls} tool calls")
            if stats:
                footer_lines.append(" · ".join(stats))
        else:
            body = ""

        if output_file:
            footer_lines.append(f"full transcript: {output_file}")

        meta_summary = _format_usage_summary(agent_id, usage_stats)
        if meta_summary:
            footer_lines.append(meta_summary)

    # TaskOutput with JSONL content — parse and extract summary
    elif _is_jsonl(content_text or ""):
        final_text, output_file, num_tool_calls, num_messages = _extract_jsonl_summary(content_text)
        body = final_text

        # Build stats line
        stats_parts = []
        if num_messages:
            stats_parts.append(f"{num_messages} turns")
        if num_tool_calls:
            stats_parts.append(f"{num_tool_calls} tool calls")
        meta_summary = _format_usage_summary(agent_id, usage_stats)
        if meta_summary:
            stats_parts.append(meta_summary)
        if stats_parts:
            footer_lines.append(" · ".join(stats_parts))
        if output_file:
            footer_lines.append(f"full transcript: {output_file}")
    else:
        meta_summary = _format_usage_summary(agent_id, usage_stats)
        if meta_summary:
            footer_lines.append(meta_summary)

    # Render result box
    header_text = f" {label} "
    box_width = max(len(header_text) + 2, 60)
    color = Colors.RED if is_error else Colors.BRIGHT_CYAN

    print(colorize(f"   ╔{'═' * box_width}╗", color))
    print(colorize(f"   ║ 🤖 {label}{' ' * (box_width - len(header_text) - 3)}║", color))
    print(colorize(f"   ╠{'═' * box_width}╣", color))

    if not body:
        print(colorize(f"   ║ {'(no output)' :<{box_width - 1}}║", color))
    else:
        for line in body.split("\n"):
            if line.startswith("# "):
                styled = colorize(line, Colors.BOLD, Colors.BRIGHT_WHITE)
            elif line.startswith("## "):
                styled = colorize(line, Colors.BOLD, Colors.BRIGHT_CYAN)
            elif line.startswith("### "):
                styled = colorize(line, Colors.BOLD, Colors.YELLOW)
            elif line.startswith("- ") or line.startswith("* "):
                styled = colorize(line, Colors.WHITE)
            elif line.startswith("> "):
                styled = colorize(line, Colors.DIM, Colors.ITALIC)
            else:
                styled = colorize(line, Colors.BRIGHT_WHITE)
            print(f"   {colorize('║', color)} {styled}")

    for fl in footer_lines:
        print(colorize(f"   ╟─ {fl}", Colors.DIM))

    print(colorize(f"   ╚{'═' * box_width}╝", color))


def render_tool_result(msg: dict) -> None:
    """Render a tool result with full content."""
    result = msg.get("tool_use_result", {})
    content = msg.get("message", {}).get("content", [{}])[0]
    content_text = content.get("content", "")
    # Normalize: content can be a list of blocks instead of a plain string
    if isinstance(content_text, list):
        content_text = "\n".join(
            block.get("text", "") if isinstance(block, dict) else str(block)
            for block in content_text
        )
    is_error = content.get("is_error", False)
    tool_use_id = content.get("tool_use_id", "")

    # Look up the original tool call
    original_call = tool_calls.get(tool_use_id, {})
    tool_name = original_call.get("name", "")
    tool_input = original_call.get("input", {})

    # Sub-agent results get distinct rendering
    tool_kind = classify_tool(tool_name, tool_input) if tool_name else ""
    if tool_kind in ("Task", "TaskOutput"):
        render_subagent_result(tool_input, content_text, is_error)
        return

    # TodoWrite results: already shown in tool_use, skip
    if tool_kind == "TodoWrite" and not is_error:
        return

    # Grep results: summary only (match count + file count)
    if tool_kind == "Grep" and not is_error and content_text:
        lines = content_text.strip().split("\n")
        # Count non-empty, non-context lines (actual matches have line numbers)
        match_lines = [l for l in lines if l and re.match(r'^\d+[:|-]', l)]
        num_matches = len(match_lines)
        # Count unique file paths (files_with_matches mode returns bare paths)
        file_paths = [l for l in lines if l and not re.match(r'^\d+[:|-]', l) and not l.startswith("[") and not l.startswith("Found ")]
        # Also look for "Found N total" summary line
        found_summary = re.search(r'Found (\d+) total occurrences? across (\d+) files?', content_text)
        if found_summary:
            total_occ = found_summary.group(1)
            total_files = found_summary.group(2)
            print(colorize(f"   ✓ {total_occ} matches across {total_files} files", Colors.GREEN))
        elif num_matches:
            print(colorize(f"   ✓ {num_matches} matching lines", Colors.GREEN))
        elif file_paths:
            print(colorize(f"   ✓ {len(file_paths)} files", Colors.GREEN))
        else:
            print(colorize(f"   ✓ 0 matches", Colors.DIM))
        return

    # Read results: summary only
    if tool_kind == "Read" and not is_error and content_text:
        num_lines = content_text.count("\n") + 1
        num_bytes = len(content_text.encode("utf-8"))
        print(colorize(f"   ✓ {num_lines} lines ({format_bytes(num_bytes)})", Colors.GREEN))
        return

    # WebSearch results: query + link count + bytes
    if tool_kind == "WebSearch" and not is_error and content_text:
        link_count = len(re.findall(r'"url"\s*:', content_text))
        num_bytes = len(content_text.encode("utf-8"))
        print(colorize(f"   ✓ {link_count} links ({format_bytes(num_bytes)})", Colors.GREEN))
        return

    # WebFetch results: bytes only
    if tool_kind == "WebFetch" and not is_error and content_text:
        num_bytes = len(content_text.encode("utf-8"))
        print(colorize(f"   ✓ fetched ({format_bytes(num_bytes)})", Colors.GREEN))
        return

    if is_error:
        # Show command for Bash errors
        if tool_name == "Bash":
            command = tool_input.get("command", "")
            if command:
                print(colorize(f"   $ {command}", Colors.MAGENTA))
        # Filter out sibling error noise and empty lines
        error_lines = [
            l for l in content_text.split("\n")
            if l.strip() and "Sibling tool call errored" not in l
        ]
        # Strip XML tags from error text
        error_lines = [re.sub(r'<[^>]+>', '', l).strip() for l in error_lines]
        error_lines = [l for l in error_lines if l]
        error_msg = "; ".join(error_lines) if len(error_lines) <= 2 else "\n".join(f"   {l}" for l in error_lines)
        if len(error_lines) <= 2:
            print(colorize(f"   ❌ {error_msg}", Colors.RED))
        else:
            print(colorize(f"   ❌ Error:", Colors.RED))
            print(colorize(error_msg, Colors.RED))
    elif isinstance(result, dict):
        # Check if it's a Bash result (has stdout/stderr)
        if "stdout" in result or "stderr" in result:
            # Show the command that was run
            if tool_name == "Bash":
                command = tool_input.get("command", "")
                if command:
                    print(colorize(f"   $ {command}", Colors.MAGENTA))
            stdout = result.get("stdout", "")
            stderr = result.get("stderr", "")
            interrupted = result.get("interrupted", False)

            # Infer exit code
            if interrupted:
                exit_code = 130  # SIGINT
                print(colorize(f"   ⚠ Exit {exit_code} (interrupted):", Colors.YELLOW))
            elif stderr and not stdout:
                exit_code = 1
                print(colorize(f"   ❌ Exit {exit_code}:", Colors.RED))
            else:
                exit_code = 0
                print(colorize(f"   ✓ Exit {exit_code}:", Colors.GREEN))

            if stdout:
                # Check if this is bd/beads output (markdown)
                command = tool_input.get("command", "")
                is_beads_cmd = command.startswith(("bd ", "beads "))
                # Beads output markers: bullets, headers, or DESCRIPTION section
                stdout_start = stdout.strip()[:100]
                is_markdown = (
                    stdout_start.startswith(("○", "●", "#", "**")) or
                    "DESCRIPTION" in stdout_start or
                    "\n## " in stdout or
                    "\n### " in stdout
                )

                print(colorize("   ┌─ stdout:", Colors.GREEN))
                if is_beads_cmd or is_markdown:
                    render_markdown(stdout, indent="   │ ")
                else:
                    for line in stdout.split("\n"):
                        print(colorize(f"   │ {line}", Colors.DIM))
                print(colorize("   └─", Colors.GREEN))
            if stderr:
                print(colorize("   ┌─ stderr:", Colors.RED))
                for line in stderr.split("\n"):
                    print(colorize(f"   │ {line}", Colors.RED))
                print(colorize("   └─", Colors.RED))
        elif result.get("file"):
            # Read operation - show summary only
            file_info = result["file"]
            path = file_info.get("filePath", "")
            file_content = file_info.get("content", "")
            num_lines = file_info.get("numLines", file_content.count("\n") + 1 if file_content else 0)
            num_bytes = len(file_content.encode("utf-8")) if file_content else 0
            print(colorize(f"   ✓ Read {num_lines} lines ({format_bytes(num_bytes)}) from {path}", Colors.GREEN))
        elif result.get("filenames"):
            filenames = result["filenames"]
            print(colorize(f"   ┌─ Found {len(filenames)} files:", Colors.GREEN))
            for f in filenames:
                print(colorize(f"   │ {f}", Colors.DIM))
            print(colorize("   └─", Colors.GREEN))
        elif content_text:
            # Dict result but actual content is in the content field (e.g. TaskOutput)
            print(colorize("   ┌─ Result:", Colors.GREEN))
            for line in content_text.split("\n"):
                print(colorize(f"   │ {line}", Colors.DIM))
            print(colorize("   └─", Colors.GREEN))
        else:
            print(colorize(f"   ✓ Done", Colors.GREEN))
    elif content_text:
        # Check if it's a beads/Skill output (often markdown)
        is_beads = tool_name == "Skill" and "beads" in str(tool_input.get("skill", ""))
        is_markdown = content_text.strip().startswith(("#", "**", "- ", "* ", "|"))

        if is_beads or is_markdown:
            print(colorize("   ┌─ Result:", Colors.GREEN))
            render_markdown(content_text, indent="   │ ")
            print(colorize("   └─", Colors.GREEN))
        else:
            # Show the full content for other results
            print(colorize("   ┌─ Result:", Colors.GREEN))
            for line in content_text.split("\n"):
                print(colorize(f"   │ {line}", Colors.DIM))
            print(colorize("   └─", Colors.GREEN))
    else:
        print(colorize(f"   ✓ Done", Colors.GREEN))


def render_assistant_message(msg: dict) -> None:
    """Render assistant messages (text and tool_use)."""
    content_blocks = msg.get("message", {}).get("content", [])

    for block in content_blocks:
        block_type = block.get("type", "")

        if block_type == "text":
            text = block.get("text", "")
            if text.strip():
                print()
                # Render markdown-ish text
                for line in text.split("\n"):
                    if line.startswith("# "):
                        print(colorize(line, Colors.BOLD, Colors.WHITE))
                    elif line.startswith("## "):
                        print(colorize(line, Colors.BOLD, Colors.CYAN))
                    elif line.startswith("- ") or line.startswith("* "):
                        print(apply_inline_emphasis("  " + line))
                    elif line.startswith("```"):
                        print(colorize(line, Colors.DIM))
                    else:
                        print(apply_inline_emphasis(line))
                print()

        elif block_type == "tool_use":
            render_tool_use(block)


def render_user_message(msg: dict) -> None:
    """Render user messages (typically tool results)."""
    content_blocks = msg.get("message", {}).get("content", [])

    for block in content_blocks:
        block_type = block.get("type", "")

        if block_type == "tool_result":
            render_tool_result(msg)
        elif block_type == "text":
            text = block.get("text", "")
            if text.strip():
                # Context compression summaries — show as system event, not user input
                if "continued from a previous conversation" in text or "ran out of context" in text:
                    print()
                    print(colorize("🔄 Context compressed — session continued with summary", Colors.BOLD, Colors.YELLOW))
                    print()
                else:
                    print(colorize(f"👤 User: {text}", Colors.BRIGHT_WHITE))


def render_result_message(msg: dict) -> None:
    """Render final result message."""
    print()
    print(colorize("━" * 60, Colors.DIM))
    print(colorize("SESSION COMPLETE", Colors.BOLD, Colors.GREEN))

    result = msg.get("result", "")
    if result:
        print(colorize(f"  Result: {result}", Colors.WHITE))

    cost = msg.get("cost_usd") or msg.get("total_cost_usd")
    if cost:
        print(colorize(f"  Cost: ${cost:.4f}", Colors.DIM))

    duration = msg.get("duration_ms")
    if duration:
        print(colorize(f"  Duration: {format_duration(duration)}", Colors.DIM))

    num_turns = msg.get("num_turns")
    if num_turns:
        print(colorize(f"  Turns: {num_turns}", Colors.DIM))

    # Show per-model usage breakdown
    model_usage = msg.get("modelUsage", {})
    for model_name, usage in model_usage.items():
        input_t = usage.get("inputTokens", 0)
        output_t = usage.get("outputTokens", 0)
        cache_r = usage.get("cacheReadInputTokens", 0)
        model_cost = usage.get("costUSD", 0)

        # Short model name
        short_name = model_name.split("-")[0:2]
        short_name = "-".join(short_name) if short_name else model_name

        parts = [f"tok: {input_t:,}↑↓{output_t:,}"]
        if cache_r:
            parts.append(f"cache: {cache_r:,}")
        if model_cost:
            parts.append(f"${model_cost:.4f}")

        print(colorize(f"  {short_name}: ", Colors.DIM), end="")
        print(colorize(" | ".join(parts), Colors.WHITE))

    print(colorize("━" * 60, Colors.DIM))


# Track tool calls by ID to display command with result
tool_calls: dict[str, dict] = {}


def process_line(line: str) -> None:
    """Process a single JSONL line."""
    try:
        msg = json.loads(line)
    except json.JSONDecodeError:
        return

    msg_type = msg.get("type", "")

    if msg_type == "system":
        render_system_message(msg)
    elif msg_type == "assistant":
        # Track tool calls for later matching with results
        for block in msg.get("message", {}).get("content", []):
            if block.get("type") == "tool_use":
                tool_calls[block.get("id", "")] = block
        render_assistant_message(msg)
    elif msg_type == "user":
        render_user_message(msg)
    elif msg_type == "result":
        render_result_message(msg)


def main() -> None:
    """Main entry point."""
    # Read from file argument or stdin
    if len(sys.argv) > 1:
        filepath = sys.argv[1]
        try:
            with open(filepath, "r") as f:
                for line in f:
                    line = line.strip()
                    if line:
                        process_line(line)
                        sys.stdout.flush()
        except FileNotFoundError:
            print(f"Error: File not found: {filepath}", file=sys.stderr)
            sys.exit(1)
    else:
        for line in sys.stdin:
            line = line.strip()
            if line:
                process_line(line)
                sys.stdout.flush()


if __name__ == "__main__":
    main()
