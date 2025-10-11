import pytest
from src.reasoning_body.reason import analyze_logic

def test_analyze():
    assert "Conclusion: [-1]" in analyze_logic("x + 1 => 0")
