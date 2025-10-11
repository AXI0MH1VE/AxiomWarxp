#!/usr/bin/env python3
"""
Reasoning Body: Logical analysis via sympy.
"""

from sympy import symbols, solve

def analyze_logic(premise: str) -> str:
    x = symbols('x')
    eq = eval(premise.replace("=>", "-"))  # Safe eval stub
    solution = solve(eq, x)
    return f"Conclusion: {solution}"

if __name__ == "__main__":
    print(analyze_logic("x + 1 => 0"))
