"""
Hooks component for SuperClaude hook scripts installation
"""

from typing import Dict, List, Tuple, Optional, Any
from pathlib import Path
import shutil

from ..core.base import Component
from ..services.claude_md import CLAUDEMdService
from setup import __version__

class HooksComponent(Component):
    """SuperClaude hooks component"""

    def __init__(self, install_dir: Optional[Path] = None):
        """Initialize hooks component"""
        super().__init__(install_dir)
        # Override component files to include all hook files
        self.component_files = [
            "anth.py",
            "elevenlabs_tts.py",
            "oai.py",
            "ollama.py",
            "openai_tts.py",
            "pyttsx3_tts.py",
            "post_tool_use.py",
            "notification.py",
            "stop.py",
            "pre_tool_use.py",
            "session_start.py",
            "subagent_stop.py",
            "plan_monitor.py",
            "pre_compact.py",
            "user_prompt_submit.py",
            "utils/llm/oai.py",
            "utils/llm/anth.py",
            "utils/llm/ollama.py",
            "utils/tts/pyttsx3_tts.py",
            "utils/tts/openai_tts.py",
            "utils/tts/elevenlabs_tts.py"
        ]

    def get_metadata(self) -> Dict[str, str]:
        """Get component metadata"""
        return {
            "name": "hooks",
            "version": __version__,
            "description": "SuperClaude hook scripts for Claude Code automation",
            "category": "automation"
        }

    def _install(self, config: Dict[str, Any]) -> bool:
        """Install hooks component"""
        self.logger.info("Installing SuperClaude hooks...")

        # Create hooks directory
        hooks_dir = self.install_dir / "hooks"
        if not self.file_manager.ensure_directory(hooks_dir):
            return False

        # Create utils subdirectories
        utils_llm_dir = hooks_dir / "utils" / "llm"
        utils_tts_dir = hooks_dir / "utils" / "tts"

        if not self.file_manager.ensure_directory(utils_llm_dir):
            return False
        if not self.file_manager.ensure_directory(utils_tts_dir):
            return False

        # Install hook files
        source_dir = self._get_source_dir()

        for file_name in self.component_files:
            source_path = source_dir / file_name
            dest_path = hooks_dir / file_name

            if not source_path.exists():
                self.logger.warning(f"Source hook file not found: {file_name}")
                continue

            # Ensure destination directory exists
            dest_path.parent.mkdir(parents=True, exist_ok=True)

            if not self.file_manager.copy_file(source_path, dest_path):
                self.logger.error(f"Failed to copy hook file: {file_name}")
                return False

            # Make hook scripts executable
            if file_name.endswith('.py') and not file_name.startswith('utils/'):
                try:
                    dest_path.chmod(0o755)
                    self.logger.debug(f"Made executable: {file_name}")
                except Exception as e:
                    self.logger.warning(f"Could not make {file_name} executable: {e}")

        return super()._install(config)

    def _post_install(self) -> bool:
        """Post-installation tasks"""
        try:
            # Add component registration to metadata
            self.settings_manager.add_component_registration("hooks", {
                "version": __version__,
                "category": "automation",
                "files_count": len(self.component_files)
            })

            self.logger.info("Updated metadata with hooks component registration")
            return True

        except Exception as e:
            self.logger.error(f"Failed to update metadata: {e}")
            return False

    def uninstall(self) -> bool:
        """Uninstall hooks component"""
        try:
            self.logger.info("Uninstalling SuperClaude hooks component...")

            # Remove hooks directory
            hooks_dir = self.install_dir / "hooks"
            removed_count = 0

            if hooks_dir.exists():
                for file_name in self.component_files:
                    file_path = hooks_dir / file_name
                    if self.file_manager.remove_file(file_path):
                        removed_count += 1
                        self.logger.debug(f"Removed {file_name}")

                # Remove empty directories
                for subdir in ["utils/llm", "utils/tts", "utils"]:
                    subdir_path = hooks_dir / subdir
                    if subdir_path.exists() and not any(subdir_path.iterdir()):
                        subdir_path.rmdir()
                        self.logger.debug(f"Removed empty directory: {subdir}")

                # Remove hooks directory if empty
                if not any(hooks_dir.iterdir()):
                    hooks_dir.rmdir()
                    self.logger.debug("Removed hooks directory")

            # Update metadata to remove hooks component
            try:
                if self.settings_manager.is_component_installed("hooks"):
                    self.settings_manager.remove_component_registration("hooks")
                    self.logger.info("Removed hooks component from metadata")
            except Exception as e:
                self.logger.warning(f"Could not update metadata: {e}")

            self.logger.success(f"Hooks component uninstalled ({removed_count} files removed)")
            return True

        except Exception as e:
            self.logger.exception(f"Unexpected error during hooks uninstallation: {e}")
            return False

    def get_dependencies(self) -> List[str]:
        """Get component dependencies"""
        return ["core"]  # Hooks depend on core framework being installed

    def update(self, config: Dict[str, Any]) -> bool:
        """Update hooks component"""
        try:
            self.logger.info("Updating SuperClaude hooks component...")

            # Check current version
            current_version = self.settings_manager.get_component_version("hooks")
            target_version = self.get_metadata()["version"]

            if current_version == target_version:
                self.logger.info(f"Hooks component already at version {target_version}")
                return True

            self.logger.info(f"Updating hooks component from {current_version} to {target_version}")

            # Perform installation (overwrites existing files)
            success = self.install(config)

            if success:
                self.logger.success(f"Hooks component updated to version {target_version}")

            return success

        except Exception as e:
            self.logger.exception(f"Unexpected error during hooks update: {e}")
            return False

    def validate_installation(self) -> Tuple[bool, List[str]]:
        """Validate hooks component installation"""
        errors = []

        # Check if hooks directory exists
        hooks_dir = self.install_dir / "hooks"
        if not hooks_dir.exists():
            errors.append("Hooks directory not found")
            return False, errors

        # Check if critical hook files exist
        critical_hooks = [
            "pre_tool_use.py",
            "post_tool_use.py",
            "session_start.py",
            "notification.py"
        ]

        for hook_file in critical_hooks:
            file_path = hooks_dir / hook_file
            if not file_path.exists():
                errors.append(f"Missing critical hook file: {hook_file}")
            elif not file_path.is_file():
                errors.append(f"Hook file is not a regular file: {hook_file}")

        # Check utils directory structure
        utils_dir = hooks_dir / "utils"
        if not utils_dir.exists():
            errors.append("Hooks utils directory not found")
        else:
            for subdir in ["llm", "tts"]:
                subdir_path = utils_dir / subdir
                if not subdir_path.exists():
                    errors.append(f"Missing utils subdirectory: {subdir}")

        # Check metadata registration
        if not self.settings_manager.is_component_installed("hooks"):
            errors.append("Hooks component not registered in metadata")
        else:
            # Check version matches
            installed_version = self.settings_manager.get_component_version("hooks")
            expected_version = self.get_metadata()["version"]
            if installed_version != expected_version:
                errors.append(f"Version mismatch: installed {installed_version}, expected {expected_version}")

        return len(errors) == 0, errors

    def _get_source_dir(self):
        """Get source directory for hook files"""
        # Assume we're in SuperClaude/setup/components/hooks.py
        # and hook files are in SuperClaude/SuperClaude/Hooks/
        project_root = Path(__file__).parent.parent.parent
        return project_root / "SuperClaude" / "Hooks"

    def get_size_estimate(self) -> int:
        """Get estimated installation size"""
        total_size = 0
        source_dir = self._get_source_dir()

        for filename in self.component_files:
            file_path = source_dir / filename
            if file_path.exists():
                total_size += file_path.stat().st_size

        # Add overhead for directories
        total_size += 5120  # ~5KB overhead

        return total_size

    def get_installation_summary(self) -> Dict[str, Any]:
        """Get installation summary"""
        return {
            "component": self.get_metadata()["name"],
            "version": self.get_metadata()["version"],
            "files_installed": len(self.component_files),
            "hook_files": self.component_files,
            "estimated_size": self.get_size_estimate(),
            "install_directory": str(self.install_dir / "hooks"),
            "dependencies": self.get_dependencies()
        }