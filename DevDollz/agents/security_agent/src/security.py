#!/usr/bin/env python3
"""
Security Agent: Scans for vulns via bandit.
"""

import subprocess

def scan_vulns(folder="."):
    result = subprocess.run(["bandit", "-r", folder], capture_output=True, text=True)
    return result.stdout + result.stderr

if __name__ == "__main__":
    print(scan_vulns())
