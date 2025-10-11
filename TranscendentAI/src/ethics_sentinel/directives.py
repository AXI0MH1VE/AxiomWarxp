#!/usr/bin/env python3
"""
Ethics Sentinel: Immutable list checks.
"""

directives = ("Be ethical", "Do no harm")  # Tuple for immutability

def check_directives(directive):
    if directive in directives:
        return "Compliant"
    else:
        return "Non-compliant"

if __name__ == "__main__":
    directive = input("Directive: ")
    print(check_directives(directive))
