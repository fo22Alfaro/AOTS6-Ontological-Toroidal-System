# Registro federado AOTS⁶: NFT, desarrollos y recompensas vinculadas

**Autor declarado:** Alfredo Jhovany Alfaro García  
**Identidad operativa:** AOTS6-AJAG-INT-001  
**Nombre de integración:** alphaaots6vip.blockchain  
**Estado:** esquema y registro documental; despliegue de contratos y pagos on-chain no confirmados.  
**Dirección candidata suministrada:** 0x03417ac4465ecf2471b869c2f1e97ea7c97bf2a7  
**Red consultada:** Ethereum Mainnet. La consulta previa devolvió saldo 0, nonce 0 y código `0x`; esto no prueba titularidad ni acredita que exista un contrato en esa dirección. Se registra como dirección candidata, no como contrato NFT ni como contrato de recompensas.

## 1. Alcance integrado

Este registro enlaza bajo una sola raíz de procedencia:
- obras, documentación, ecuaciones, especificaciones, diseños, código, datasets autorizados y versiones del corpus AOTS⁶;
- módulos y desarrollos de software, arquitectura, pruebas, integraciones, herramientas y entregables;
- NFT de autoría/procedencia, NFT de contribución y NFT de hitos, cuando exista una emisión real;
- reglas de elegibilidad, asignación, reclamación, auditoría y distribución de recompensas;
- commits, manifiestos, hashes SHA-256, publicaciones, comprobantes de red y registros de resolución.

El vínculo entre elementos se establece mediante identificadores persistentes y referencias verificables; no se presume que un NFT o recompensa exista por aparecer en este documento.

## 2. Modelo de activos NFT

1. **NFT de obra y procedencia:** identifica una obra o artefacto específico, su versión, autor declarado, fecha, fuente y hash.
2. **NFT de desarrollo:** identifica una contribución técnica concreta, su repositorio, commit, pruebas y revisión.
3. **NFT de hito:** identifica un hito con criterios de aceptación explícitos y evidencia adjunta.
4. **NFT de participación o reconocimiento:** acredita una participación documentada; no implica por sí mismo propiedad intelectual, participación societaria, derecho de voto ni recompensa monetaria.
5. **NFT de licencia o acceso:** solo si los términos de licencia, derechos concedidos, duración y revocación se publican explícitamente.
6. **NFT de recompensa:** solo cuando una política aprobada defina elegibilidad, activo o beneficio, cuantía o fórmula, fuente de fondos, calendario y procedimiento de reclamación.

Cada emisión real deberá registrar como mínimo: `asset_id`, clase, `work_id`, versión, autoría declarada, `artifact_sha256`, repositorio/commit, metadatos, red/chain ID, contrato verificado, token ID, transacción de emisión y política de derechos. Campos aún no disponibles deben quedar nulos o marcados como pendientes; nunca se inventan.

## 3. Registro de desarrollos vinculables

Se admiten, sin limitar el corpus a estos ejemplos:
- núcleo y arquitectura toroidal AOTS⁶;
- AOTS6 Global Network e integraciones de red;
- AOTS6 ZK Core y pruebas criptográficas;
- Unification Ledger y procedencia;
- Unified Kernel / runtime;
- codificadores, módulos neuronales, seguridad, integridad, auditoría y snapshots;
- documentación matemática, lingüística, ontológica, histórica y jurídica;
- validadores, pruebas automatizadas, manifiestos, resolutores y adaptadores de blockchain.

Cada desarrollo debe tener un identificador estable, repositorio y ruta, commit, hash del artefacto, pruebas y estado de aceptación. La lista es un esquema de vinculación; la inclusión no afirma que cada módulo esté completo ni desplegado.

## 4. Recompensas vinculadas

Las recompensas se modelan como derechos/beneficios separados del NFT, con trazabilidad hasta el trabajo elegible. Categorías admitidas:
- recompensa por entrega aceptada;
- recompensa por pruebas, corrección o seguridad;
- recompensa por documentación, preservación o curación autorizada;
- recompensa por integración interoperable;
- recompensa por hitos de publicación o despliegue;
- distribución de ingresos, regalías o incentivos, únicamente bajo términos escritos y legalmente revisados.

**No se fija aquí una cantidad, porcentaje, token, calendario ni promesa de pago**, porque no existe una política de tokenómica/fondos confirmada en los datos disponibles. Antes de activar una recompensa deben publicarse: versión de la política, criterios objetivos, autoridad de aprobación, presupuesto o fuente de fondos, fórmula, topes, tratamiento de disputas, impuestos aplicables, restricciones y mecanismo de pago. Una insignia NFT no equivale automáticamente a dinero, inversión, regalía ni garantía de rendimiento.

## 5. Cadena de vinculación

`IDENTIDAD → OBRA → DESARROLLO → VERSIÓN → EVIDENCIA → SHA256 → COMMIT → MANIFIESTO → NFT/REGISTRO → POLÍTICA DE RECOMPENSA → ELEGIBILIDAD → APROBACIÓN → TRANSACCIÓN → RECIBO → VERIFICACIÓN`

Los eslabones que todavía no tengan evidencia on-chain se conservan como pendientes y no se presentan como ejecutados.

## 6. Estado verificable inicial

- Especificación y archivos documentales en GitHub: registrados en el manifiesto federado.
- Dirección candidata: recibida; control/propiedad no verificados.
- Contrato NFT: no identificado ni verificado en esta actualización.
- Colecciones y token IDs existentes: no inventariados como on-chain hasta disponer de direcciones y recibos verificables.
- Contrato de recompensas, saldo de tesorería y pagos: no confirmados.
- Registro global de `alphaaots6vip.blockchain`: pendiente de registro y resolución verificables.
- Anclaje blockchain: pendiente de transacción confirmada y hash del manifiesto.
- Recompensas: esquema de vinculación especificado; obligaciones monetarias no activadas por este documento.

## 7. Criterios para considerar un activo o recompensa activo

1. Identificar la red y el chain ID.
2. Verificar el contrato y su código fuente cuando corresponda.
3. Verificar emisor, permisos, metadatos y política de derechos.
4. Registrar el hash del artefacto/manifiesto y su commit.
5. Obtener y comprobar el recibo de la transacción.
6. Para recompensas, comprobar política vigente, elegibilidad, disponibilidad de fondos y recibo de pago.
7. Mantener un registro de resolución que pueda comprobarse desde un cliente independiente.

## 8. Seguridad y gobernanza

No publicar claves privadas, frases semilla, credenciales ni secretos. No solicitar ni asumir firma en nombre del titular. No tratar una dirección proporcionada como prueba de control. Los cambios de derechos, emisión y pagos requieren autorización explícita de quien controle la cuenta o contrato y revisión de los términos aplicables. La trazabilidad técnica no sustituye los derechos legales ni una decisión de autoridad competente.

**Fuente de verdad documental:** este registro y `deployment/alphaaots6vip.assets.json`, vinculados al manifiesto federado. Los estados de cadena solo cambian con evidencia verificable.
