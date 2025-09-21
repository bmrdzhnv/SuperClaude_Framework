#!/usr/bin/env python3
"""
ASDF Auto-Fix Utility
Automatically creates/updates .tool-versions file when asdf version errors occur.
"""

import os
import re
import subprocess
import sys
from pathlib import Path
from typing import Optional, Tuple, Dict, List


def parse_asdf_error(error_message: str) -> Optional[Tuple[str, str]]:
    """
    Parse asdf error message to extract tool and suggested version.

    Returns:
        Tuple of (tool_name, suggested_version) or None if not parseable
    """
    # Pattern: "No version is set for command [tool]"
    tool_pattern = r"No version is set for command (\w+)"
    tool_match = re.search(tool_pattern, error_message)

    if not tool_match:
        return None

    tool = tool_match.group(1)

    # Pattern to find version suggestions (e.g., "uv 0.8.17")
    version_pattern = rf"{tool}\s+([\d.]+)"
    version_match = re.search(version_pattern, error_message)

    if version_match:
        return (tool, version_match.group(1))

    return None


def get_installed_versions(tool: str) -> List[str]:
    """
    Get list of installed versions for a tool via asdf.

    Returns:
        List of installed version strings
    """
    try:
        result = subprocess.run(
            ["asdf", "list", tool],
            capture_output=True,
            text=True,
            check=False
        )

        if result.returncode != 0:
            return []

        # Parse output (format: "  version" or "* version" for current)
        versions = []
        for line in result.stdout.strip().split('\n'):
            line = line.strip()
            if line.startswith('*'):
                line = line[1:].strip()
            if line:
                versions.append(line)

        return versions
    except Exception:
        return []


def read_tool_versions(path: Path) -> Dict[str, str]:
    """
    Read existing .tool-versions file.

    Returns:
        Dictionary of tool -> version mappings
    """
    tools = {}

    if path.exists():
        try:
            with open(path, 'r') as f:
                for line in f:
                    line = line.strip()
                    if line and not line.startswith('#'):
                        parts = line.split(None, 1)
                        if len(parts) == 2:
                            tools[parts[0]] = parts[1]
        except Exception:
            pass

    return tools


def write_tool_versions(path: Path, tools: Dict[str, str]) -> bool:
    """
    Write .tool-versions file.

    Returns:
        True if successful, False otherwise
    """
    try:
        # Create backup if file exists
        if path.exists():
            backup_path = path.with_suffix('.tool-versions.bak')
            backup_path.write_text(path.read_text())

        # Write new file
        lines = []
        for tool, version in sorted(tools.items()):
            lines.append(f"{tool} {version}")

        path.write_text('\n'.join(lines) + '\n')
        return True
    except Exception as e:
        print(f"Error writing .tool-versions: {e}", file=sys.stderr)
        return False


def fix_asdf_version(tool: str, version: str, project_path: Optional[Path] = None) -> bool:
    """
    Fix asdf version for a tool by updating .tool-versions.

    Args:
        tool: Tool name (e.g., 'uv', 'python')
        version: Version to set
        project_path: Path to project directory (default: current directory)

    Returns:
        True if successful, False otherwise
    """
    if project_path is None:
        project_path = Path.cwd()

    tool_versions_path = project_path / '.tool-versions'

    # Check if version is installed
    installed = get_installed_versions(tool)
    if version not in installed:
        print(f"Warning: {tool} version {version} not installed via asdf", file=sys.stderr)
        print(f"Available versions: {', '.join(installed)}", file=sys.stderr)

        # Use first available version if suggested not installed
        if installed:
            version = installed[0]
            print(f"Using installed version: {version}", file=sys.stderr)
        else:
            print(f"No {tool} versions installed. Run: asdf install {tool} {version}", file=sys.stderr)
            return False

    # Read existing tool versions
    tools = read_tool_versions(tool_versions_path)

    # Update tool version
    tools[tool] = version

    # Write updated file
    success = write_tool_versions(tool_versions_path, tools)

    if success:
        print(f"✓ Added {tool} {version} to {tool_versions_path}")

    return success


def auto_fix_from_error(error_message: str, project_path: Optional[Path] = None) -> bool:
    """
    Automatically fix asdf version error from error message.

    Returns:
        True if fixed successfully, False otherwise
    """
    parsed = parse_asdf_error(error_message)

    if not parsed:
        return False

    tool, version = parsed
    return fix_asdf_version(tool, version, project_path)


def run_with_asdf_fix(command: List[str], max_retries: int = 2) -> subprocess.CompletedProcess:
    """
    Run command and auto-fix asdf errors if they occur.

    Args:
        command: Command to run as list
        max_retries: Maximum number of fix attempts

    Returns:
        CompletedProcess result from final attempt
    """
    for attempt in range(max_retries):
        result = subprocess.run(
            command,
            capture_output=True,
            text=True
        )

        # Check for asdf error (exit code 126)
        if result.returncode == 126:
            error_output = result.stderr + result.stdout

            if "No version is set for command" in error_output:
                print(f"Detected asdf version error, attempting auto-fix...")

                if auto_fix_from_error(error_output):
                    print(f"Auto-fix successful, retrying command...")
                    continue
                else:
                    print(f"Auto-fix failed", file=sys.stderr)
                    break

        # Return result if not asdf error or if fix failed
        return result

    return result


def main():
    """CLI interface for manual fixes."""
    import argparse

    parser = argparse.ArgumentParser(description="ASDF Auto-Fix Utility")
    parser.add_argument(
        "tool",
        nargs="?",
        help="Tool name to fix (e.g., uv, python)"
    )
    parser.add_argument(
        "version",
        nargs="?",
        help="Version to set"
    )
    parser.add_argument(
        "--from-error",
        action="store_true",
        help="Read error from stdin and auto-fix"
    )
    parser.add_argument(
        "--path",
        type=Path,
        help="Project path (default: current directory)"
    )

    args = parser.parse_args()

    if args.from_error:
        # Read error from stdin
        error_message = sys.stdin.read()
        success = auto_fix_from_error(error_message, args.path)
        sys.exit(0 if success else 1)
    elif args.tool and args.version:
        # Manual fix
        success = fix_asdf_version(args.tool, args.version, args.path)
        sys.exit(0 if success else 1)
    else:
        parser.print_help()
        sys.exit(1)


if __name__ == "__main__":
    main()