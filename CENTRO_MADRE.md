# AOTS6 - CENTRO MADRE

El Centro Madre es la capa de integración verificable del repositorio. Registra los componentes existentes y separa evidencia implementada, integración externa y bloqueos criptográficos reales.

Estados:
1. implemented: existe implementación o artefacto verificable.
2. integration_only / implemented_record / evidence_referenced: existe interfaz, registro o referencia, pero no se declara una ejecución externa sin evidencia.
3. blocked_pending_keyed_signature: requiere una operación criptográfica con la clave privada autorizada.

Componentes integrados:
- geometría toroidal;
- grafo ontológico;
- proveniencia y raíz de artefactos;
- runtime criptográfico;
- registro de estado cuántico;
- ingestión QKD externa;
- envelope ZK-SNARK externo;
- anclajes externos referenciados;
- autenticación de red.

Regla de precisión:
QKD requiere material generado por un sistema QKD real. ZK-SNARK requiere su sistema probador/verificador. Una firma sólo se declara válida cuando existe una firma criptográfica verificable.

AOTS6_NET_AUTH.sig queda explícitamente pendiente si está vacío. No se genera una firma falsa ni se reutiliza una clave privada no disponible.

Verificación:
    python -m centro_madre.verify

El registro incluye SHA-256 y tamaño de cada artefacto presente.
