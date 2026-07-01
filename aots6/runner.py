#!/usr/bin/env python3
"""
AOTS6 - Runner Module (SAFE MODE)
Ejecutor de ciclos controlados de monitoreo
Autor: ALFREDO JHOVANY ALFARO GARCIA
"""

import time
import requests
from aots6.core_state_machine import AOTS6Core

class AOTS6Runner:
    def __init__(self):
        self.core = AOTS6Core()
        self.endpoint = "https://api.dexscreener.com/latest/dex/search?q=QR"
        self.headers = {
            "User-Agent": "AOTS6-Runner/1.0",
            "Accept": "application/json"
        }

    def probe(self):
        try:
            r = requests.get(self.endpoint, headers=self.headers, timeout=5)

            if r.status_code != 200:
                self.core.probe_result(False, f"HTTP_{r.status_code}")
                return

            data = r.json()
            pairs = data.get("pairs", [])

            if not pairs:
                self.core.probe_result(False, "EMPTY_RESPONSE")
                return

            pair = pairs[0]
            volume = float(pair.get("volume", {}).get("h24", 0))

            if volume <= 0:
                self.core.probe_result(False, "ZERO_VOLUME")
                return

            self.core.probe_result(True)
            print(f"[OK] Volume 24h: {volume}")

        except requests.exceptions.Timeout:
            self.core.probe_result(False, "TIMEOUT")
        except requests.exceptions.ConnectionError:
            self.core.probe_result(False, "CONNECTION_ERROR")
        except Exception as e:
            self.core.probe_result(False, f"CRITICAL:{str(e)}")

    def run(self, cycles=3, delay=5):
        """
        Safe execution mode:
        - finite cycles instead of infinite loop
        - controlled delay between probes
        """
        for i in range(cycles):
            print(f"\n[Cycle {i+1}/{cycles}]")
            self.probe()
            time.sleep(delay)


if __name__ == "__main__":
    runner = AOTS6Runner()
    runner.run()
