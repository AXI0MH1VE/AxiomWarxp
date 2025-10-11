#!/usr/bin/env python3
"""
Monitoring Agent: Tracks metrics, alerts on thresholds.
"""

import psutil
import time

def monitor_cpu(threshold: float = 80.0):
    while True:
        usage = psutil.cpu_percent()
        if usage > threshold:
            print(f"ALERT: CPU {usage}%")
        time.sleep(5)

if __name__ == "__main__":
    monitor_cpu()
