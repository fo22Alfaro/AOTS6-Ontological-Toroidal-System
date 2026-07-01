#!/usr/bin/env python3
"""
AOTS6 - Core State Machine Module
Autor: ALFREDO JHOVANY ALFARO GARCIA
Modelo: AOTS6
"""

import os
import json
import time
import hashlib
from datetime import datetime

STATE_FILE = "aots6_state.json"
LOG_FILE = "aots6_forensics.log"

class AOTS6Core:
    def __init__(self):
        self.state = "NORMAL"
        self.anomaly_level = 0
        self.last_event = None
        self.load_state()

    # --------------------
    # Persistence
    # --------------------
    def load_state(self):
        if os.path.exists(STATE_FILE):
            try:
                with open(STATE_FILE, "r") as f:
                    data = json.load(f)
                    self.state = data.get("state", "NORMAL")
                    self.anomaly_level = data.get("anomaly_level", 0)
            except:
                self.state = "NORMAL"
                self.anomaly_level = 0

    def save_state(self):
        data = {
            "state": self.state,
            "anomaly_level": self.anomaly_level,
            "timestamp": datetime.utcnow().isoformat()
        }
        with open(STATE_FILE, "w") as f:
            json.dump(data, f, indent=4)

    # --------------------
    # Forensics
    # --------------------
    def log_event(self, event):
        payload = f"{time.time()}|{event}"
        hash_event = hashlib.sha256(payload.encode()).hexdigest()
        line = f"{payload}|{hash_event}\n"
        with open(LOG_FILE, "a") as f:
            f.write(line)

    # --------------------
    # State logic
    # --------------------
    def transition(self, new_state, reason=""):
        self.log_event(f"STATE:{self.state}->{new_state}:{reason}")
        self.state = new_state
        self.save_state()

    def register_anomaly(self, reason):
        self.anomaly_level += 1
        self.log_event(f"ANOMALY:{reason}:{self.anomaly_level}")

        if self.anomaly_level >= 3:
            self.transition("DEFENSE", "THRESHOLD_REACHED")

    def recover(self):
        self.anomaly_level = 0
        self.transition("NORMAL", "RECOVERY")

    # --------------------
    # External probe hook
    # --------------------
    def probe_result(self, ok=True, reason=""):
        if not ok:
            self.register_anomaly(reason)
        else:
            if self.state == "DEFENSE":
                self.recover()

    # --------------------
    # Status
    # --------------------
    def status(self):
        return {
            "state": self.state,
            "anomaly_level": self.anomaly_level
        }
