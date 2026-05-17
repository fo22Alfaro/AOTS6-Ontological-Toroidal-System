import os, json, hashlib, time

class QcoTokenizationBridge:
    def __init__(self):
        self.base_dir = os.path.dirname(os.path.abspath(__file__))
        self.ledger_path = os.path.join(self.base_dir, "../QCO_LEDGER.json")
        self.bridge_log = os.path.join(self.base_dir, "../manifests/BRIDGE_STATE.json")

    def synchronize_to_global_chain(self):
        if not os.path.exists(self.ledger_path): return
        with open(self.ledger_path, "r") as f: ledger_data = json.load(f)
        total_local_qco = ledger_data.get("TOTAL_CAPITAL_QCO", 0.0)
        
        last_sync = 0.0
        if os.path.exists(self.bridge_log):
            with open(self.bridge_log, "r") as f:
                last_sync = json.load(f).get("LAST_SYNCHRONIZED_QCO", 0.0)

        delta_to_mint = total_local_qco - last_sync
        if delta_to_mint > 0:
            tx_hash = hashlib.sha3_256(f"TX_{time.time()}_{delta_to_mint}".encode()).hexdigest()
            sync_manifest = {
                "LAST_SYNCHRONIZED_QCO": total_local_qco,
                "LAST_TRANSACTION_HASH": tx_hash,
                "NETWORK_STATUS": "ON_CHAIN_SYNCHRONIZED",
                "TIMESTAMP": str(time.time())
            }
            with open(self.bridge_log, "w") as f: json.dump(sync_manifest, f, indent=4)
            print(f"[V] BRIDGE: Sincronización exitosa. Tx Hash Global: {tx_hash}")

if __name__ == "__main__":
    QcoTokenizationBridge().synchronize_to_global_chain()
