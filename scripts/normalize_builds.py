"""
Normalizes build scripts for cross-platform compatibility.
"""

from pathlib import Path
import re

class BuildNormalizer:
    """Fixes common build script issues."""

    @staticmethod
    def fix_line_endings(file_path: Path) -> None:
        """Converts CRLF to LF for Unix compatibility."""
        content = file_path.read_bytes()
        content = content.replace(b'\r\n', b'\n')
        file_path.write_bytes(content)
        print(f"Fixed line endings: {file_path}")

    @staticmethod
    def fix_cargo_toml(cargo_toml: Path) -> None:
        """Validates and fixes Cargo.toml syntax."""
        content = cargo_toml.read_text()

        # Fix common issues
        fixes = [
            (r'release\s*$', 'release]'),  # Missing bracket
            (r'\s+$', ''),  # Trailing whitespace
        ]

        for pattern, replacement in fixes:
            content = re.sub(pattern, replacement, content, flags=re.MULTILINE)

        cargo_toml.write_text(content)
        print(f"Fixed Cargo.toml: {cargo_toml}")

    @staticmethod
    def create_build_script(project_root: Path) -> None:
        """Creates unified cross-platform build script."""
        build_script = project_root / "build.py"

        script_content = '''#!/usr/bin/env python3
"""
Unified build script for AxiomHive.
Handles all platform-specific build logic.
"""

import subprocess
import sys
from pathlib import Path

def build_rust_components():
    """Builds Rust AgentMatrix."""
    print("Building Rust components...")
    result = subprocess.run(
        ["cargo", "build", "--release"],
        cwd="AgentMatrix",
        capture_output=True,
        text=True
    )
    if result.returncode != 0:
        print(f"Rust build failed:\\n{result.stderr}")
        sys.exit(1)
    print("Rust build complete")

def build_python_components():
    """Compiles Python modules."""
    print("Building Python components...")
    result = subprocess.run(
        [sys.executable, "-m", "compileall", ".", "-q"],
        capture_output=True,
        text=True
    )
    if result.returncode != 0:
        print(f"Python compile failed:\\n{result.stderr}")
        sys.exit(1)
    print("Python build complete")

def run_tests():
    """Executes test suite."""
    print("Running tests...")
    result = subprocess.run(
        [sys.executable, "-m", "pytest", "-v"],
        capture_output=True,
        text=True
    )
    print(result.stdout)
    if result.returncode != 0:
        print(f"Some tests failed")
    else:
        print("All tests passed")

if __name__ == "__main__":
    build_rust_components()
    build_python_components()
    run_tests()
    print("\\nBuild complete!")
'''

        build_script.write_text(script_content)
        build_script.chmod(0o755)
        print(f"Created build script: {build_script}")

# Execute normalization
if __name__ == "__main__":
    normalizer = BuildNormalizer()
    project_root = Path.cwd()

    # Fix line endings in all source files
    for ext in ['*.py', '*.rs', '*.toml', '*.sh']:
        for file in project_root.rglob(ext):
            normalizer.fix_line_endings(file)

    # Fix Cargo.toml
    cargo_toml = project_root / "AgentMatrix" / "Cargo.toml"
    if cargo_toml.exists():
        normalizer.fix_cargo_toml(cargo_toml)

    # Create unified build script
    normalizer.create_build_script(project_root)
