#!/usr/bin/env python3
"""
Entropy Matrix Harmonizer: Weighted avg synth.
"""

import numpy as np

def synthesize(values, weights):
    return np.average(values, weights=weights)

if __name__ == "__main__":
    values = [1, 2, 3]
    weights = [0.5, 0.3, 0.2]
    print(synthesize(values, weights))
