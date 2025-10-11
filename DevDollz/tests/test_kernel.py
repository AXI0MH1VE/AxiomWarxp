#!/usr/bin/env python3
"""
Pytest suite for DevDollz Kernel.
"""

import pytest
from devdollz_kernel.src.main import Kernel

def test_orchestrate():
    kernel = Kernel()
    # Mock docker
    assert kernel.agents  # Non-empty

if __name__ == "__main__":
    pytest.main([__file__])
