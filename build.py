#!/usr/bin/env python3
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
        print(f"Rust build failed:\n{result.stderr}")
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
        print(f"Python compile failed:\n{result.stderr}")
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
    print("\nBuild complete!")
