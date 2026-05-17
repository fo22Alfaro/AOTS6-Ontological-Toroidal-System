# -*- coding: utf-8 -*-
# ==============================================================================
# SYSTEM: AOTS6 ONTOLOGICAL TOROIDAL SYSTEM
# MODULE: AUTOMATED CRITICAL STATE DAEMON
# AUTHOR: Alfredo Jhovany Alfaro García (AAGA3)
# HORIZON: 200-YEAR POST-QUANTUM IMMUNITY
# ==============================================================================

import os
import sys
import time
import json
import hashlib

# Asegurar la importación del núcleo criptográfico unificado
sys.path.append(os.path.abspath(os.path.dirname(__file__)))
try:
    from aoalfaro_core import DilithiumAoAlfaroSigner
except ImportError:
    print("[!] ERROR: No se encontró 'aoalfaro_core.py' en el directorio core.")
    sys.exit(1)

def main():
    # Verificación Ontológica de Capa 5
    if os.environ.get("AOTS6_STATUS") != "SOVEREIGN":
        print("[!] ERROR CRÍTICO: El demonio requiere autoridad PDC-1 activa.")
        sys.exit(1)

    print("[AOTS6-DAEMON] Inicializando ciclo perpetuo de cristalización...")
    signer = DilithiumAoAlfaroSigner()
    
    # Resolver la ruta absoluta de la carpeta de manifiestos anclada
    base_dir = os.path.dirname(os.path.abspath(__file__))
    manifest_dir = os.path.abspath(os.path.join(base_dir, "../manifests"))
    
    # Leer secuencia inicial para evitar colisiones cronológicas
    sequence = 1
    
    print(f"[V] Flujo toroidal activo. Destino: {manifest_dir}")
    
    while True:
        try:
            # Forjar el pulso de datos atómico (Telemetría de estado)
            current_time = time.time()
            telemetry = f"AOTS6_PULSE_SEQ_{sequence}_METAPLEX_ACTIVE_{current_time}".encode()
            
            # Generar el manifiesto post-cuántico híbrido
            sealed_manifest = signer.generate_sealed_state(telemetry, state_sequence=sequence)
            
            # Derivar un índice de archivo no lineal basado en el hash del timestamp
            file_identifier = hashlib.sha256(sealed_manifest["TIMESTAMP"].encode()).hexdigest()[:12]
            filename = f"AOTS6_STATE_{sequence:06d}_{file_identifier}.json"
            filepath = os.path.join(manifest_dir, filename)
            
            # Escribir de forma síncrona en el almacenamiento físico
            with open(filepath, "w", encoding="utf-8") as f:
                json.dump(sealed_manifest, f, indent=4)
                
            print(f"[+] [\u03A6] Estado {sequence} sellado con éxito en -> {filename}")
            
            # Incrementar el índice de la línea temporal
            sequence += 1
            
            # Intervalo armónico basado en el retardo de fase (Frecuencia de muestreo)
            time.sleep(60)
            
        except KeyboardInterrupt:
            print("\n[!] Demonio suspendido por el operador Origen.")
            sys.exit(0)
        except Exception as e:
            print(f"[!] Anomalía interceptada en el bucle del tensor: {e}")
            time.sleep(5)

if __name__ == "__main__":
    main()
