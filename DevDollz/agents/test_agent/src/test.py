#!/usr/bin/env python3
"""
Test Agent: Pytest wrapper.
"""

import pytest

def run_tests():
    pytest.main(["--tb=short", "tests/"])

if __name__ == "__main__":
    run_tests()
