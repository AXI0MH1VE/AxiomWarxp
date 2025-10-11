#!/usr/bin/env python3
"""
Safety Guardian: OODA loop with rate limit.
"""

import time

class OODALoop:
    def __init__(self, rate_limit_per_second=10):
        self.rate_limit = rate_limit_per_second
        self.last_call = 0

    def observe(self):
        # Observe environment
        return "Observation"

    def orient(self, obs):
        # Orient with data
        return "Orientation"

    def decide(self, ori):
        # Decide action
        return "Decision"

    def act(self, dec, rate_limit_check):
        if not rate_limit_check:
            return "Rate limited"
        # Act
        return "Action taken"

    def loop(self):
        now = time.time()
        rate_ok = (now - self.last_call) >= (1 / self.rate_limit)
        if rate_ok:
            self.last_call = now
            obs = self.observe()
            ori = self.orient(obs)
            dec = self.decide(ori)
            result = self.act(dec, True)
        else:
            result = "Rate limited"
        return result

if __name__ == "__main__":
    ooda = OODALoop()
    print(ooda.loop())
