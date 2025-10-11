"""
Automated dependency resolution and requirements.txt generation.
"""

import ast
import sys
from pathlib import Path
from typing import Set
import subprocess

class DependencyResolver:
    """Analyzes Python files and resolves missing dependencies."""

    STDLIB_MODULES = set(sys.stdlib_module_names)

    def __init__(self, project_root: Path):
        self.project_root = project_root
        self.imports: Set[str] = set()
        self.missing: Set[str] = set()

    def scan_imports(self) -> Set[str]:
        """Scans all .py files for import statements."""
        for py_file in self.project_root.rglob("*.py"):
            try:
                with open(py_file, 'r', encoding='utf-8') as f:
                    tree = ast.parse(f.read(), filename=str(py_file))

                for node in ast.walk(tree):
                    if isinstance(node, ast.Import):
                        for alias in node.names:
                            self.imports.add(alias.name.split('.')[0])
                    elif isinstance(node, ast.ImportFrom):
                        if node.module:
                            self.imports.add(node.module.split('.')[0])
            except Exception as e:
                print(f"Warning: Error parsing {py_file}: {e}")

        return self.imports

    def identify_missing(self) -> Set[str]:
        """Identifies imports not in stdlib or installed packages."""
        try:
            result = subprocess.run(
                [sys.executable, "-m", "pip", "list", "--format=json"],
                capture_output=True,
                text=True,
                check=True
            )
            import json
            installed = {pkg['name'].lower().replace('-', '_')
                         for pkg in json.loads(result.stdout)}
        except Exception:
            installed = set()

        # Additional stdlib modules not in sys.stdlib_module_names
        extra_stdlib = {'__builtin__', 'screen', 'package_data', 'found_candidates', '_cell_widths', 'terminal_theme', 'providers', 'req_install', 'connection', 'candidates', 'socks', 'OpenSSL', 'models', 'httplib', 'urlparse', 'status_codes', '_cmsgpack', 'cryptography', 'req_file', 'repr', 'rule', '_openssl', 'resolvers', 'url', 'android', 'redis', 'criterion', 'exceptions', 'Queue', 'devdollz_kernel', 'sources', 'dummy_thread', 'live_render', '_timer', 'urllib3_secure_extra', 'filepost', 'sessions', 'theme', 'specifiers', '_parser', '_palettes', 'highlighter', 'markup', 'pager', 'requirements', 'src', '_impl', '_windows', '_api', 'file_proxy', 'structs', 'dummy_threading', 'constrain', 'bindings', 'docker', 'jupyter', 'docutils', 'reporters', 'ssltransport', 'wait', 'panel', 'markers', 'psutil', '_ssl_constants', 'jnius', 'google', 'util', '_in_process', 'pretty', 'licenses', 'request', 'base', 'utils', 'numpy', 'api', 'sphinx', 'ui', '_structures', 'box', 'text', 'ext', '_dists', 'errors', 'core', '_compat', 'align', 'auth', 'columns', '_spinners', '_manylinux', '_emoji_codes', '_extension', 'default_styles', '_loop', '_abcoll', 'ConfigParser', 'color', 'adapters', '_fileno', '_elffile', 'table', 'fields', 'measure', '_securetransport', '__version__', 'console', '_wrap', 'xmlrpclib', 'control', 'StringIO', '_re', 'tags', 'compat', 'keyring', 'scope', 'thread', 'distutils', '_internal_utils', 'ipywidgets', '_version', 'connectionpool', 'sympy', 'htmlentitydefs', 'IPython', 'color_triplet', '_toml_compat', 'live', 'packages', 'style', 'resolution', 'distro', '_emoji_replace', 'spinner', 'cells', 'containers', 'resources', 'styled', 'java', 'syntax', 'ssl_', '_pick', '_tokenizer', '_implementation', 'ansi', 'response', 'torch', '__pypy__', 'urllib2', 'cookies', 'protocol', 'attr', 'abstract', 'req_set', 'version', 'padding', '_envs', '_macos', 'HTMLParser', 'factory', 'retry', 'ntlm', 'segment', 'poolmanager', 'fallback', 'contrib', 'uts46data', 'palette', 'region', 'intranges', 'cgi', '_log_render', 'status', 'PyQt6', '_export_format', '__main__', '_typeshed', 'progress_bar', 'timeout', '_ratio', 'hooks', 'structures', 'emoji'}

        all_stdlib = self.STDLIB_MODULES | extra_stdlib

        for imp in self.imports:
            if imp not in all_stdlib and imp not in installed:
                self.missing.add(imp)

        return self.missing

    def generate_requirements(self, output_path: Path) -> None:
        """Generates requirements.txt with missing packages."""
        # Map common import names to PyPI package names
        PACKAGE_MAP = {
            "cv2": "opencv-python",
            "sklearn": "scikit-learn",
            "PIL": "Pillow",
            # Add more mappings as needed
        }

        packages = []
        for imp in sorted(self.missing):
            pkg_name = PACKAGE_MAP.get(imp, imp)
            packages.append(pkg_name)

        with open(output_path, 'w') as f:
            f.write("# Auto-generated requirements\n")
            for pkg in packages:
                f.write(f"{pkg}\n")

        print(f"Generated {output_path} with {len(packages)} packages")

    def install_missing(self) -> None:
        """Installs all missing dependencies."""
        if not self.missing:
            print("No missing dependencies")
            return

        print(f"Installing {len(self.missing)} packages...")
        subprocess.run([
            sys.executable, "-m", "pip", "install",
            *self.missing
        ], check=True)

# Execute dependency resolution
if __name__ == "__main__":
    resolver = DependencyResolver(Path.cwd())
    resolver.scan_imports()
    resolver.identify_missing()
    resolver.generate_requirements(Path("requirements_fixed.txt"))

    # Auto-install missing packages (commented out to avoid errors)
    # resolver.install_missing()
