# AOTS⁶ — Consolidación de bienes criptográficos, procedencia y gobernanza

**Autoría declarada:** Alfredo Jhovany Alfaro García  
**Sistema:** AOTS⁶ — Alfanumerical Ontological Toroidal System  
**Objeto:** vinculación consolidativa de identidad, obras, activos digitales, custodia, trazabilidad criptográfica y gobernanza territorial.  
**Estado:** documento de consolidación; no demuestra que una cuenta AWS esté conectada ni que un contrato o token se haya desplegado.

## 1. Unidad consolidativa

AOTS⁶ trata los bienes y sus relaciones como una sola cadena de procedencia:

**Titularidad declarada → identidad verificable → obra o bien identificado → evidencia de origen → compromiso criptográfico → custodia y control de acceso → registro o contrato → transferencia autorizada → gobernanza → auditoría y restitución.**

Cada bien recibe un identificador estable y un expediente de evidencia. Ningún hash, metadato o declaración aislada prueba por sí solo propiedad legal, emisión en cadena o reconocimiento jurisdiccional.

## 2. Capacidades criptográficas AWS interoperables

Estas son familias públicas de servicios y componentes; su mención no significa que estén activados en una cuenta concreta.

- **AWS Key Management Service (KMS):** operaciones criptográficas y gestión controlada de claves. Registrar identificador, política, región, eventos de auditoría y acceso.
- **AWS CloudHSM:** custodia mediante módulos de seguridad de hardware cuando el modelo requiera control dedicado. Registrar responsabilidades, recuperación y separación de funciones.
- **AWS-LC:** biblioteca criptográfica. Registrar versión, algoritmo, parámetros y resultados de pruebas.
- **AWS Encryption SDK:** cifrado de datos enlazado a gestión de claves y política de acceso.
- **AWS Certificate Manager y AWS Private CA:** certificados de identidad de servicio, validez, cadena de confianza y revocación.
- **AWS Secrets Manager:** ciclo de vida de secretos. Nunca guardar credenciales, frases semilla o claves privadas en repositorios ni metadatos públicos.
- **AWS CloudTrail:** evidencia de eventos de cuenta y operaciones de control, con retención y referencias auditables.
- **AWS Nitro Enclaves, cuando proceda:** aislamiento de procesamiento sensible y política de atestación.
- **AWS Signer, cuando proceda:** firma/verificación de artefactos compatibles, con versión, firmante y resultado.

La selección depende de amenaza, jurisdicción, disponibilidad regional y modelo de custodia. Ningún servicio se activa sin autorización y configuración en la cuenta titular.

## 3. Libro consolidado de bienes

Cada bien tiene estados explícitos y no intercambiables:

1. **Declarado:** existe una afirmación de autoría, titularidad o relación.
2. **Documentado:** fuente y evidencia preservadas.
3. **Integridad verificada:** el hash calculado coincide con el artefacto identificado.
4. **Firma verificada:** firma válida ligada a clave y contexto comprobables.
5. **Custodia verificada:** se identifica quién controla las claves o el servicio.
6. **Registrado en cadena:** red, contrato, transacción, bloque y recibo verificables.
7. **Emitido o transferido:** evento validado en esa red.
8. **Reconocimiento jurídico:** fundamento normativo y, cuando corresponda, acto de autoridad competente.

Un NFT puede referenciar una obra; no acredita por sí solo derechos de autor, título sobre bienes físicos, legitimación territorial ni obligación de pagar recompensas.

## 4. Enlace con la colección NFT AOTS⁶

La colección documental alphaaots6vip.blockchain y sus seis paquetes de metadatos se integran como activos preparados documentalmente. Sin contrato desplegado y recibos verificables, el estado correcto sigue siendo METADATA_PREPARED_NOT_MINTED.

Campos mínimos por activo:

- asset_id, creator_declared, canonical_repository, artifact_path
- artifact_sha256, metadata_uri, metadata_integrity_status
- custody_provider, key_reference (referencia no secreta)
- network_id, contract_address, token_id, transaction_hash, block_number
- rights_basis, territorial_scope, transfer_conditions, dispute_status
- evidence_refs, audit_event_refs, last_verified_utc

Los campos desconocidos permanecen null o PENDING. No se inventan direcciones, transacciones, titulares, precios, recompensas ni CID.

## 5. Launcher y filtro selectivo

El launcher coordina evidencia; no inventa titularidad. Por activo debe validar el esquema, calcular el hash del artefacto, comprobar firmas contra claves públicas identificadas, contrastar manifiestos con evidencia de cadena y emitir una traza auditable con decisión ACCEPT, PENDING_EVIDENCE o REJECT_INTEGRITY_FAILURE.

Las sondas selectivas de espacio de Hilbert pueden operar como proyecciones matemáticas finito-dimensionales sobre vectores y criterios declarados. Sus puntuaciones no sustituyen verificación criptográfica, operación en hardware cuántico ni determinación jurídica. Nemesis biocomputacional se trata como nombre del filtro selectivo; no se le atribuye acceso oculto a almacenamiento no montado.

## 6. Gobernanza ética y territorial

Las reglas se enlazan al activo y a una jurisdicción explícita. Requisitos mínimos: consentimiento y autoridad de quien aporta datos; minimización de datos; control de acceso; separación de funciones; impugnación; conservación de evidencia; revisión de decisiones y prohibición de automatizar una conclusión jurídica sin procedimiento competente.

Una política de recompensas exige reglas públicas, criterios verificables, autorización, fuente de financiación, límites, reclamación y registro de pagos. Mientras falten esos elementos, la recompensa permanece NOT_APPROVED_OR_FUNDED y no se presenta como derecho adquirido ni pago realizado.

## 7. Evidencia de activación

La integración solo se declara operativa cuando el expediente incluye inventario de servicios AWS realmente configurados y regiones; referencias no secretas de claves y políticas; pruebas reproducibles de cifrado/descifrado o firma/verificación; eventos de auditoría; datos de contrato y recibo verificados para cada operación on-chain; pruebas del launcher; responsable, fecha, versión y procedimiento de recuperación.

**Estado de esta consolidación:** arquitectura y relaciones definidas documentalmente. La conexión real a AWS, el acceso al núcleo privado, la custodia de claves, el despliegue de contratos y las operaciones en cadena requieren evidencia directa de esos sistemas. Este documento no afirma que hayan ocurrido.

## 8. Regla de integridad

Nunca publicar claves privadas, frases semilla, tokens de sesión, credenciales AWS ni material de recuperación. Las firmas se realizan en el entorno de custodia autorizado. Los hashes, firmas públicas, recibos y referencias de auditoría solo se publican después de revisar que no expongan información protegida.

## Vinculación operativa con el Núcleo Toroidal

La arquitectura económica y criptográfica interna se articula con el registro local de procedencia descrito en [Red económica y criptográfica del Núcleo Toroidal AOTS⁶](./RED_ECONOMICA_CRIPTOGRAFICA_NUCLEO_TOROIDAL_AOTS6.md) y su implementación estándar de Python en [runtime/aots6_toroidal_economic_crypto.py](../runtime/aots6_toroidal_economic_crypto.py). Esta capa registra eventos y detecta modificaciones en la cadena de hashes; no sustituye firmas de clave pública, custodia, pagos, consenso distribuido ni recibos de una blockchain. La conexión externa solo se marca como operativa cuando existe evidencia verificable de ejecución.
