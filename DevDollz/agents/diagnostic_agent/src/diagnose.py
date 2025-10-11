#!/usr/bin/env python3
"""
Diagnostic Agent: Fault tree analysis on logs.
"""

import sys

def diagnose_logs(logs: str) -> str:
    if "ERROR" in logs and "MEMORY" in logs:
        return "Memory error"
    elif "TIMEOUT" in logs:
        return "Timeout issue"
    else:
        return "No diagnosis"

if __name__ == "__main__":
    logs = input()
    print(diagnose_logs(logs))
