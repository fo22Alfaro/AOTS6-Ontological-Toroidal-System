import os, json, glob
from http.server import HTTPServer, BaseHTTPRequestHandler

class Aots6DashboardHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        
        # Recolectar datos
        base_dir = os.path.dirname(os.path.abspath(__file__))
        ledger = {}
        try:
            with open(os.path.join(base_dir, "../QCO_LEDGER.json"), "r") as f: ledger = json.load(f)
        except: ledger = {"TOTAL_CAPITAL_QCO": 0.0}
        
        manifest_count = len(glob.glob(os.path.join(base_dir, "../manifests/*.json")))
        captures = []
        for f in glob.glob(os.path.join(base_dir, "../captures/*.json")):
            with open(f, "r") as c: captures.append(json.load(c))

        html = f"""
        <html><head><title>AOTS6 Dashboard</title>
        <style>
            body {{ background: #020617; color: #38bdf8; font-family: 'Courier New', monospace; padding: 20px; }}
            .card {{ border: 1px solid #0d9488; padding: 15px; margin-bottom: 20px; background: #0f172a; }}
            h1 {{ color: #0d9488; text-transform: uppercase; border-bottom: 2px solid #0d9488; }}
            .stat {{ font-size: 24px; font-weight: bold; color: #facc15; }}
            table {{ width: 100%; border-collapse: collapse; margin-top: 10px; }}
            th, td {{ border: 1px solid #1e293b; padding: 8px; text-align: left; }}
            th {{ background: #1e293b; color: #0d9488; }}
        </style></head>
        <body>
            <h1>AOTS6 Sovereign Dashboard <small>(AAGA3 PDC-1)</small></h1>
            <div class="card">
                <h3>Reserva de Capital</h3>
                <div class="stat">{ledger.get("TOTAL_CAPITAL_QCO", 0.0)} QCO</div>
                <p>Masa Crítica Acumulada: {manifest_count} Bloques</p>
            </div>
            <div class="card">
                <h3>Horizonte de Eventos (Capturas de Seguridad)</h3>
                <table>
                    <tr><th>Origen IP</th><th>Timestamp</th><th>Status</th></tr>
                    {"".join([f"<tr><td>{c['THREAT_IP']}</td><td>{c['TIMESTAMP']}</td><td>{c['STATUS']}</td></tr>" for c in captures])}
                </table>
            </div>
            <div class="card">
                <h3>System Integrity: SEALED_BY_AAGA3</h3>
            </div>
        </body></html>"""
        self.wfile.write(html.encode())

def run():
    httpd = HTTPServer(('', 8888), Aots6DashboardHandler)
    print("[+] Dashboard ACTIVO en http://localhost:8888")
    httpd.serve_forever()

if __name__ == "__main__": run()
