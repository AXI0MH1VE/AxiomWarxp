"""
Cross-platform command compatibility layer.
Replaces bash-style commands with Python equivalents.
"""

import os
import sys
import subprocess
from pathlib import Path
from typing import List, Optional

class PlatformCompat:
    """Provides cross-platform command abstractions."""

    @staticmethod
    def open_file(filepath: str) -> None:
        """Opens file with default system application."""
        file_path = Path(filepath).resolve()
        if not file_path.exists():
            raise FileNotFoundError(f"File not found: {file_path}")

        if sys.platform == "win32":
            os.startfile(str(file_path))
        elif sys.platform == "darwin":
            subprocess.run(["open", str(file_path)])
        else:
            subprocess.run(["xdg-open", str(file_path)])

    @staticmethod
    def chain_commands(commands: List[str], cwd: Optional[Path] = None) -> int:
        """
        Executes commands sequentially (replaces && chaining).
        Stops on first failure.
        """
        for cmd in commands:
            result = subprocess.run(
                cmd,
                shell=True,
                cwd=cwd,
                capture_output=True,
                text=True
            )
            if result.returncode != 0:
                print(f"❌ Command failed: {cmd}")
                print(f"   Error: {result.stderr}")
                return result.returncode
        return 0

    @staticmethod
    def execute_sql_script(db_path: str, script_path: str) -> None:
        """Executes SQL script (replaces sqlite3 < redirection)."""
        import sqlite3

        with open(script_path, 'r') as f:
            sql_script = f.read()

        conn = sqlite3.connect(db_path)
        try:
            conn.executescript(sql_script)
            conn.commit()
        finally:
            conn.close()

# Usage examples
if __name__ == "__main__":
    compat = PlatformCompat()

    # Replace: open AxiomHive/STRATEGY.md
    compat.open_file("AxiomHive/STRATEGY.md")

    # Replace: cd AgentMatrix && cargo build --release
    compat.chain_commands([
        "cd AgentMatrix",
        "cargo build --release"
    ])

    # Replace: sqlite3 db.sqlite < schema.sql
    compat.execute_sql_script("db.sqlite", "schema.sql")
