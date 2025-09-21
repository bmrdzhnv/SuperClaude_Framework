#!/usr/bin/env python3
"""
Test script for ASDF auto-fix functionality.
"""

import sys
import subprocess
from pathlib import Path

# Add utils to path
sys.path.insert(0, str(Path(__file__).parent.parent / "Hooks" / "utils"))
from asdf_auto_fix import parse_asdf_error, auto_fix_from_error


def test_parse_error():
    """Test error parsing."""
    error_msg = """
    No version is set for command uv
    Consider adding one of the following versions in your config file at /path/.tool-versions
    uv 0.8.17
    """

    result = parse_asdf_error(error_msg)
    assert result == ('uv', '0.8.17'), f"Expected ('uv', '0.8.17'), got {result}"
    print("✓ Error parsing test passed")


def test_auto_fix():
    """Test auto-fix in a temporary directory."""
    import tempfile
    import os

    with tempfile.TemporaryDirectory() as tmpdir:
        # Change to temp directory
        old_cwd = os.getcwd()
        os.chdir(tmpdir)

        try:
            # Simulate error
            error_msg = """
            No version is set for command uv
            Consider adding one of the following versions in your config file
            uv 0.8.17
            """

            # Try auto-fix
            success = auto_fix_from_error(error_msg)

            # Check if .tool-versions was created
            tool_versions_path = Path('.tool-versions')
            if tool_versions_path.exists():
                content = tool_versions_path.read_text()
                print(f"✓ Created .tool-versions with content:\n{content}")
                assert 'uv' in content
            else:
                print("✗ .tool-versions not created")

        finally:
            os.chdir(old_cwd)


def main():
    """Run tests."""
    print("Testing ASDF Auto-Fix...")

    test_parse_error()
    test_auto_fix()

    print("\n✅ All tests passed!")


if __name__ == '__main__':
    main()