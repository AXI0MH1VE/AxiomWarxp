#!/usr/bin/env python3
"""
CodeGen Agent: Deterministic code synthesis using sympy.
"""

from sympy import symbols, Eq, solve

def synth_code(equation: str) -> str:
    x = symbols('x')
    eq = Eq(eval(equation + "-0", {"x": symbols('x')}), 0)  # Safe eval stub
    solution = solve(eq, x)
    return f"def solution(): return {solution}"

if __name__ == "__main__":
    import sys
    equation = sys.argv[1] if len(sys.argv) > 1 else input("Enter equation: ")
    print(synth_code(equation))
