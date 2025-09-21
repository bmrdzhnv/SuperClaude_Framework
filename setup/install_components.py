#!/usr/bin/env python3
"""
Enhanced installation script for SuperClaude Framework components
Includes plan system, meta-agents, hooks, and all new features
"""

import json
import shutil
import os
import time
from pathlib import Path
from typing import Dict, List, Any
import sys


class ComponentInstaller:
    """Install SuperClaude components based on manifest"""

    def __init__(self, framework_dir: Path, target_dir: Path = None):
        self.framework_dir = framework_dir
        self.target_dir = target_dir or Path.home() / ".claude"
        self.manifest_path = framework_dir / "SuperClaude" / "installation_manifest.json"
        self.manifest = self._load_manifest()

    def _load_manifest(self) -> Dict[str, Any]:
        """Load installation manifest"""
        if not self.manifest_path.exists():
            raise FileNotFoundError(f"Manifest not found: {self.manifest_path}")

        with open(self.manifest_path, 'r') as f:
            return json.load(f)

    def _expand_path(self, path_str: str) -> Path:
        """Expand ~ and environment variables in path"""
        expanded = os.path.expanduser(os.path.expandvars(path_str))
        return Path(expanded)

    def _ensure_directory(self, path: Path) -> None:
        """Create directory if it doesn't exist"""
        path.mkdir(parents=True, exist_ok=True)

    def install_component(self, component_name: str, component_config: Dict[str, Any]) -> None:
        """Install a single component"""
        print(f"📦 Installing {component_name}...")

        source_path = self.framework_dir / "SuperClaude" / component_config["path"]
        dest_path = self._expand_path(component_config["destination"])

        # Ensure destination exists
        self._ensure_directory(dest_path)

        # Get file patterns
        patterns = component_config.get("files", ["*"])
        if not isinstance(patterns, list):
            patterns = [patterns]

        # Copy files
        for pattern in patterns:
            files = list(source_path.glob(pattern))
            if component_config.get("recursive", False):
                files.extend(source_path.rglob(pattern))

            for file in files:
                if file.is_file():
                    # Handle prefix
                    dest_name = file.name
                    if "prefix" in component_config:
                        if not dest_name.startswith(component_config["prefix"]):
                            dest_name = component_config["prefix"] + dest_name

                    dest_file = dest_path / dest_name

                    # Handle merge strategy for settings
                    if component_config.get("merge_strategy") == "smart" and dest_file.exists():
                        self._merge_settings(file, dest_file, component_config.get("backup_existing", False))
                    else:
                        # Simple copy
                        shutil.copy2(file, dest_file)
                        print(f"   ✓ {dest_name}")

                    # Make executable if needed
                    if component_config.get("make_executable", False):
                        dest_file.chmod(0o755)

        # Report new additions
        if "includes_new" in component_config:
            print(f"   🆕 New components: {', '.join(component_config['includes_new'])}")

    def _merge_settings(self, source: Path, dest: Path, backup: bool = True) -> None:
        """Smart merge of settings files"""
        if backup:
            backup_path = dest.with_suffix(f".backup_{int(time.time())}")
            shutil.copy2(dest, backup_path)
            print(f"   📋 Backed up existing settings to {backup_path.name}")

        # Load both files
        with open(source, 'r') as f:
            source_data = json.load(f)
        with open(dest, 'r') as f:
            dest_data = json.load(f)

        # Merge (source takes precedence for new keys)
        for key, value in source_data.items():
            if key not in dest_data:
                dest_data[key] = value
            elif isinstance(value, dict) and isinstance(dest_data[key], dict):
                # Recursive merge for dicts
                dest_data[key].update(value)

        # Write merged result
        with open(dest, 'w') as f:
            json.dump(dest_data, f, indent=2)

        print(f"   ✓ Merged settings successfully")

    def run_post_install(self) -> None:
        """Run post-installation tasks"""
        print("\n🔧 Running post-installation tasks...")

        post_install = self.manifest.get("post_install", {})

        # Create directories
        for dir_path in post_install.get("create_directories", []):
            path = self._expand_path(dir_path)
            self._ensure_directory(path)
            print(f"   ✓ Created directory: {path}")

        # Set permissions
        for pattern, perms in post_install.get("set_permissions", {}).items():
            path_pattern = self._expand_path(pattern)
            base_path = path_pattern.parent
            file_pattern = path_pattern.name

            if base_path.exists():
                for file in base_path.glob(file_pattern):
                    file.chmod(int(perms, 8))
                    print(f"   ✓ Set permissions {perms} on {file.name}")

        # Update CLAUDE.md
        self._update_claude_md(post_install.get("update_claude_md", {}))

    def _update_claude_md(self, config: Dict[str, Any]) -> None:
        """Update CLAUDE.md with new imports"""
        claude_md = self.target_dir / "CLAUDE.md"

        if not claude_md.exists():
            print(f"   ⚠️  CLAUDE.md not found, skipping import updates")
            return

        # Read existing content
        with open(claude_md, 'r') as f:
            content = f.read()

        # Add new imports if not present
        new_imports = config.get("add_imports", [])
        added = []

        for import_line in new_imports:
            if import_line not in content:
                # Find MCP section and add there
                mcp_marker = "# MCP Documentation"
                if mcp_marker in content:
                    lines = content.split('\n')
                    for i, line in enumerate(lines):
                        if line.strip() == mcp_marker:
                            # Find next empty line or end of section
                            j = i + 1
                            while j < len(lines) and lines[j].strip().startswith('@'):
                                j += 1
                            lines.insert(j, import_line)
                            content = '\n'.join(lines)
                            added.append(import_line)
                            break

        if added:
            with open(claude_md, 'w') as f:
                f.write(content)
            print(f"   ✓ Added imports to CLAUDE.md: {', '.join(added)}")

    def install_all(self) -> None:
        """Install all components in order"""
        print(f"🚀 Installing SuperClaude Framework v{self.manifest['version']}")
        print(f"📂 Target directory: {self.target_dir}\n")

        # Install components in specified order
        for component_name in self.manifest["installation_order"]:
            if component_name in self.manifest["components"]:
                self.install_component(component_name, self.manifest["components"][component_name])

        # Run post-installation tasks
        self.run_post_install()

        # Display summary
        self._display_summary()

    def _display_summary(self) -> None:
        """Display installation summary"""
        print("\n" + "="*50)
        print("✅ Installation Complete!")
        print("="*50)

        meta = self.manifest.get("meta", {})
        print(f"\n📋 {meta.get('description', 'SuperClaude Framework')}")

        if "added_features" in meta:
            print("\n🆕 New Features:")
            for feature in meta["added_features"]:
                print(f"   • {feature}")

        print("\n📘 Usage:")
        print("   • /sc:plan \"your task\" - Generate executable workflow")
        print("   • /execute-plan - Execute generated plans")
        print("   • /sc:research \"topic\" - Gather documentation")

        print("\n🎯 Meta-Agents Available:")
        print("   • computational-strategist - Optimal path finding")
        print("   • superclaude-framework - Orchestration")

        print("\n💡 Next Steps:")
        print("   1. Restart Claude Code to load new configuration")
        print("   2. Try: /sc:plan \"build a React component\"")
        print("   3. Check ~/.claude/plans/ for generated plans")


def main():
    """Main entry point"""
    import argparse
    import time

    parser = argparse.ArgumentParser(description="Install SuperClaude Framework components")
    parser.add_argument("--framework-dir", type=Path,
                       default=Path(__file__).parent.parent,
                       help="Path to SuperClaude framework directory")
    parser.add_argument("--target-dir", type=Path,
                       default=Path.home() / ".claude",
                       help="Target installation directory")
    parser.add_argument("--component", type=str,
                       help="Install specific component only")

    args = parser.parse_args()

    try:
        installer = ComponentInstaller(args.framework_dir, args.target_dir)

        if args.component:
            # Install specific component
            if args.component in installer.manifest["components"]:
                installer.install_component(args.component,
                                          installer.manifest["components"][args.component])
                installer.run_post_install()
                print(f"\n✅ Component '{args.component}' installed successfully!")
            else:
                print(f"❌ Component '{args.component}' not found in manifest")
                print(f"Available components: {', '.join(installer.manifest['components'].keys())}")
                sys.exit(1)
        else:
            # Install everything
            installer.install_all()

    except FileNotFoundError as e:
        print(f"❌ Error: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Installation failed: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()