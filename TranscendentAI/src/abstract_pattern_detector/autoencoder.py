#!/usr/bin/env python3
"""
Abstract Pattern Detector: PyTorch simple AE.
"""

import torch
import torch.nn as nn

class Autoencoder(nn.Module):
    def __init__(self):
        super().__init__()
        self.encoder = nn.Linear(10, 5)
        self.decoder = nn.Linear(5, 10)

    def forward(self, x):
        x = torch.relu(self.encoder(x))
        x = torch.sigmoid(self.decoder(x))
        return x

if __name__ == "__main__":
    model = Autoencoder()
    x = torch.randn(1, 10)
    y = model(x)
    print("AE output:", y)
