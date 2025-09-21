#!/usr/bin/env python3
"""
ASDF-aware Hook Runner
Wraps hook execution to handle asdf version management automatically.
"""

import sys
import subprocess
import os
from pathlib import Path

# Add utils to path for asdf_auto_fix
hook_utils = Path(__file__).parent.parent / "Hooks" / "utils"
sys.path.insert(0, str(hook_utils))

try:
    from asdf_auto_fix import run_with_asdf_fix
except ImportError:
    # Fallback if asdf_auto_fix not available
    def run_with_asdf_fix(command, **kwargs):
        return subprocess.run(command)


def main():
    """
    Run a hook script with asdf auto-fix support.

    Usage: asdf_hook_runner.py <hook_script> [args...]
    """
    if len(sys.argv) < 2:
        print("Usage: asdf_hook_runner.py <hook_script> [args...]", file=sys.stderr)
        sys.exit(1)

    hook_script = sys.argv[1]
    hook_args = sys.argv[2:] if len(sys.argv) > 2 else []

    # Determine if we should use uv or python directly
    if hook_script.endswith('.py'):
        # Check if uv is available and script needs it
        with open(hook_script, 'r') as f:
            first_line = f.readline()

        if 'uv run' in first_line or '# /// script' in f.read():
            # Use uv for scripts with uv dependencies
            command = ['uv', 'run', hook_script] + hook_args
        else:
            # Use python directly
            command = [sys.executable, hook_script] + hook_args
    else:
        # Non-Python script, execute directly
        command = [hook_script] + hook_args

    # Run with asdf auto-fix
    result = run_with_asdf_fix(command)

    # Exit with same code as hook
    sys.exit(result.returncode)


if __name__ == '__main__':
    main()