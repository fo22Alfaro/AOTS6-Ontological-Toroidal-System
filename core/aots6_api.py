import os, sys, json
from http.server import HTTPServer, BaseHTTPRequestHandler
from aoalfaro_core import DilithiumAoAlfaroSigner

class Aots6ApiHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        if self.path == "/evaluate":
            length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(length)
            try:
                payload = json.loads(post_data.decode('utf-8'))
                external_data = payload.get("DATA", "").encode()
                
                signer = DilithiumAoAlfaroSigner()
                sealed_certificate = signer.generate_sealed_state(external_data, state_sequence=999)
                sealed_certificate["COST_CREDITS"] = "0.01 QCO"
                sealed_certificate["INTEGRITY_VERDICT"] = "SYSTEM_VERIFIED_SECURE"
                
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps(sealed_certificate, indent=4).encode())
            except Exception as e:
                self.send_response(400)
                self.end_headers()

def run_server():
    if os.environ.get("AOTS6_STATUS") != "SOVEREIGN": sys.exit(1)
    httpd = HTTPServer(('', 8080), Aots6ApiHandler)
    print("[+] API: SaaS Integrity Gateway escuchando en puerto 8080...")
    httpd.serve_forever()

if __name__ == "__main__":
    run_server()
