"""
Settings component for SuperClaude settings.json installation
"""

from typing import Dict, List, Tuple, Optional, Any
from pathlib import Path
import json
import shutil

from ..core.base import Component
from setup import __version__

class SettingsComponent(Component):
    """SuperClaude settings component"""

    def __init__(self, install_dir: Optional[Path] = None):
        """Initialize settings component"""
        super().__init__(install_dir)
        # Override component files to include settings.json
        self.component_files = ["settings.json"]

    def get_metadata(self) -> Dict[str, str]:
        """Get component metadata"""
        return {
            "name": "settings",
            "version": __version__,
            "description": "SuperClaude settings configuration for Claude Code",
            "category": "configuration"
        }

    def _install(self, config: Dict[str, Any]) -> bool:
        """Install settings component"""
        self.logger.info("Installing SuperClaude settings...")

        source_dir = self._get_source_dir()
        source_path = source_dir / "settings.json"
        dest_path = self.install_dir / "settings.json"

        if not source_path.exists():
            self.logger.error("Source settings.json not found")
            return False

        # Check if destination exists for smart merging
        if dest_path.exists():
            self.logger.info("Existing settings.json found, performing smart merge...")
            if not self._smart_merge_settings(source_path, dest_path):
                return False
        else:
            # Simple copy for new installation
            if not self.file_manager.copy_file(source_path, dest_path):
                self.logger.error("Failed to copy settings.json")
                return False

        return super()._install(config)

    def _smart_merge_settings(self, source_path: Path, dest_path: Path) -> bool:
        """Smart merge SuperClaude settings with existing user settings"""
        try:
            # Create backup of existing settings
            backup_path = dest_path.with_suffix(f".backup_{int(__import__('time').time())}")
            shutil.copy2(dest_path, backup_path)
            self.logger.info(f"Created backup: {backup_path.name}")

            # Load both settings files
            with open(source_path, 'r') as f:
                superclaude_settings = json.load(f)

            with open(dest_path, 'r') as f:
                user_settings = json.load(f)

            # Merge strategy: SuperClaude adds new settings, preserves user customizations
            merged_settings = self._merge_settings_recursive(user_settings, superclaude_settings)

            # Write merged settings
            with open(dest_path, 'w') as f:
                json.dump(merged_settings, f, indent=2)

            self.logger.info("Successfully merged settings")
            return True

        except Exception as e:
            self.logger.error(f"Failed to merge settings: {e}")
            return False

    def _merge_settings_recursive(self, user_settings: Dict, superclaude_settings: Dict) -> Dict:
        """Recursively merge settings with user preferences taking priority"""
        merged = user_settings.copy()

        for key, value in superclaude_settings.items():
            if key not in merged:
                # New setting from SuperClaude
                merged[key] = value
                self.logger.debug(f"Added new setting: {key}")
            elif isinstance(value, dict) and isinstance(merged[key], dict):
                # Recursively merge nested dictionaries
                merged[key] = self._merge_settings_recursive(merged[key], value)
            elif key == "hooks" and isinstance(value, dict) and isinstance(merged[key], dict):
                # Special handling for hooks: merge hook arrays
                merged[key] = self._merge_hooks(merged[key], value)
            # For other cases, keep user's existing setting (no override)

        return merged

    def _merge_hooks(self, user_hooks: Dict, superclaude_hooks: Dict) -> Dict:
        """Merge hook configurations, adding new hooks while preserving user hooks"""
        merged_hooks = user_hooks.copy()

        for hook_type, hook_configs in superclaude_hooks.items():
            if hook_type not in merged_hooks:
                # New hook type from SuperClaude
                merged_hooks[hook_type] = hook_configs
                self.logger.debug(f"Added new hook type: {hook_type}")
            else:
                # Merge hook configurations (preserve user hooks, add new SuperClaude hooks)
                existing_commands = set()
                for config in merged_hooks[hook_type]:
                    for hook in config.get("hooks", []):
                        if "command" in hook:
                            existing_commands.add(hook["command"])

                # Add new SuperClaude hooks that don't conflict
                for config in hook_configs:
                    for hook in config.get("hooks", []):
                        if "command" in hook and hook["command"] not in existing_commands:
                            # Add to first matching config or create new one
                            if merged_hooks[hook_type]:
                                merged_hooks[hook_type][0]["hooks"].append(hook)
                            else:
                                merged_hooks[hook_type] = [{"hooks": [hook]}]
                            self.logger.debug(f"Added new hook command: {hook['command']}")

        return merged_hooks

    def _post_install(self) -> bool:
        """Post-installation tasks"""
        try:
            # Add component registration to metadata
            self.settings_manager.add_component_registration("settings", {
                "version": __version__,
                "category": "configuration",
                "files_count": len(self.component_files)
            })

            self.logger.info("Updated metadata with settings component registration")
            return True

        except Exception as e:
            self.logger.error(f"Failed to update metadata: {e}")
            return False

    def uninstall(self) -> bool:
        """Uninstall settings component"""
        try:
            self.logger.info("Uninstalling SuperClaude settings component...")

            # Note: We don't remove settings.json as it may contain user customizations
            # Instead, we just remove the component registration
            try:
                if self.settings_manager.is_component_installed("settings"):
                    self.settings_manager.remove_component_registration("settings")
                    self.logger.info("Removed settings component from metadata")
            except Exception as e:
                self.logger.warning(f"Could not update metadata: {e}")

            self.logger.success("Settings component uninstalled (settings.json preserved)")
            return True

        except Exception as e:
            self.logger.exception(f"Unexpected error during settings uninstallation: {e}")
            return False

    def get_dependencies(self) -> List[str]:
        """Get component dependencies"""
        return ["core", "hooks"]  # Settings depend on core and hooks being installed

    def update(self, config: Dict[str, Any]) -> bool:
        """Update settings component"""
        try:
            self.logger.info("Updating SuperClaude settings component...")

            # Check current version
            current_version = self.settings_manager.get_component_version("settings")
            target_version = self.get_metadata()["version"]

            if current_version == target_version:
                self.logger.info(f"Settings component already at version {target_version}")
                return True

            self.logger.info(f"Updating settings component from {current_version} to {target_version}")

            # Perform installation (smart merge)
            success = self.install(config)

            if success:
                self.logger.success(f"Settings component updated to version {target_version}")

            return success

        except Exception as e:
            self.logger.exception(f"Unexpected error during settings update: {e}")
            return False

    def validate_installation(self) -> Tuple[bool, List[str]]:
        """Validate settings component installation"""
        errors = []

        # Check if settings.json exists
        settings_path = self.install_dir / "settings.json"
        if not settings_path.exists():
            errors.append("settings.json not found")
            return False, errors

        # Validate JSON structure
        try:
            with open(settings_path, 'r') as f:
                settings_data = json.load(f)

            # Check for essential settings
            required_settings = ["permissions", "hooks"]
            for setting in required_settings:
                if setting not in settings_data:
                    errors.append(f"Missing required setting: {setting}")

            # Check hook configuration
            if "hooks" in settings_data:
                hooks = settings_data["hooks"]
                if not isinstance(hooks, dict):
                    errors.append("Hooks setting is not a dictionary")
                else:
                    # Check for essential hook types
                    essential_hooks = ["PreToolUse", "PostToolUse", "SessionStart"]
                    for hook_type in essential_hooks:
                        if hook_type not in hooks:
                            errors.append(f"Missing essential hook type: {hook_type}")

        except json.JSONDecodeError as e:
            errors.append(f"Invalid JSON in settings.json: {e}")
        except Exception as e:
            errors.append(f"Error validating settings.json: {e}")

        # Check metadata registration
        if not self.settings_manager.is_component_installed("settings"):
            errors.append("Settings component not registered in metadata")
        else:
            # Check version matches
            installed_version = self.settings_manager.get_component_version("settings")
            expected_version = self.get_metadata()["version"]
            if installed_version != expected_version:
                errors.append(f"Version mismatch: installed {installed_version}, expected {expected_version}")

        return len(errors) == 0, errors

    def _get_source_dir(self):
        """Get source directory for settings files"""
        # Assume we're in SuperClaude/setup/components/settings.py
        # and settings files are in SuperClaude/SuperClaude/Settings/
        project_root = Path(__file__).parent.parent.parent
        return project_root / "SuperClaude" / "Settings"

    def get_size_estimate(self) -> int:
        """Get estimated installation size"""
        source_dir = self._get_source_dir()
        settings_path = source_dir / "settings.json"

        if settings_path.exists():
            return settings_path.stat().st_size
        else:
            return 2048  # ~2KB estimate

    def get_installation_summary(self) -> Dict[str, Any]:
        """Get installation summary"""
        return {
            "component": self.get_metadata()["name"],
            "version": self.get_metadata()["version"],
            "files_installed": len(self.component_files),
            "settings_file": "settings.json",
            "estimated_size": self.get_size_estimate(),
            "install_directory": str(self.install_dir),
            "dependencies": self.get_dependencies(),
            "merge_strategy": "smart_merge"
        }