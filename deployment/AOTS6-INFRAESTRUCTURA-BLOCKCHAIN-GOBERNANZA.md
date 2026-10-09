# AOTS⁶ — Infraestructura blockchain, launcher y gobernanza integrada

**Responsable de la obra:** Alfredo Jhovany Alfaro García  
**Identificador operativo:** AOTS6-AJAG-INT-001  
**Sistema:** Alfanumerical Ontological Toroidal System (AOTS⁶)  
**Estado de este documento:** publicado en repositorio; no equivale a despliegue de contrato ni a autorización regulatoria.

## Cadena operativa única

`IDENTIDAD/PROCEDENCIA → MANIFIESTO → LAUNCHER → RPC/RED → CONTRATO → ACTIVO/TÍTULO → REGLAS ALGORÍTMICAS → GOBERNANZA → AUDITORÍA → EVIDENCIA DE CUMPLIMIENTO`

Cada transición produce un registro con identificador, marca temporal UTC, red, dirección de contrato cuando exista, hash de artefacto, actor autorizado, resultado y evidencia. Si falta un dato, el estado es `PENDING`; nunca se infiere un despliegue a partir de código fuente o de un commit.

## Topología y componentes

- **Raíz de procedencia:** historial Git, commits, manifiestos y archivos de metadatos NFT.
- **Launcher:** `assets/nft/scripts/deploy.js` para despliegue del contrato y `assets/nft/scripts/mint-six.js` para acuñación autorizada. Los secretos se cargan mediante variables de entorno; nunca se guardan en Git ni se comparten en el chat.
- **Contrato NFT:** `assets/nft/contracts/AOTS6AssetRegistry.sol`; colección limitada a seis identificadores según el código fuente. Compilación, pruebas y dirección desplegada deben comprobarse por separado.
- **Metadatos y arte:** `assets/nft/metadata/` y `assets/nft/images/`. Los enlaces raw de GitHub son mutables; para persistencia inmutable se requieren CID IPFS/otro almacenamiento direccionado por contenido y verificación de hash.
- **Red y RPC:** el launcher debe identificar explícitamente chain ID, RPC, dirección del firmante y red de destino. Una prueba en testnet no es una operación en mainnet.
- **Registro de activos/bienes:** cada registro distingue la obra digital, el token, el derecho contractual y el bien físico o inmueble. Un NFT por sí solo no transmite propiedad real, título registral, posesión, licencia ni derecho territorial.
- **Recompensas:** estado desactivado hasta que exista política aprobada, fuente de fondos, reglas de elegibilidad, límites, divulgación de riesgos y contrato verificable. No se prometen rendimientos ni pagos inexistentes.
- **Gobernanza territorial:** decisiones, competencias, consentimiento, límites geográficos, impugnaciones y evidencia se registran como datos auditables; el código no sustituye autoridades, registros públicos ni debido proceso.
- **Auditoría:** registrar versión del código, hash, chain ID, dirección, transacción, bloque, evento emitido, recibo, verificación del bytecode y resultado de pruebas.

## Semántica de estados

- `SOURCE_PUBLISHED`: código o documentación visible.
- `BUILD_VERIFIED`: compilación reproducible exitosa.
- `TESTS_PASSED`: pruebas ejecutadas y resultado conservado.
- `TESTNET_DEPLOYED`: transacción confirmada en red de pruebas.
- `MAINNET_DEPLOYED`: transacción confirmada en la red principal especificada y bytecode verificado.
- `MINTED`: evento de acuñación y propietario confirmados on-chain.
- `RIGHTS_DOCUMENTED`: documentos jurídicos identificados; no implica que el derecho haya sido reconocido por autoridad.
- `REGULATORY_REVIEW_REQUIRED`: clasificación jurídica pendiente para la actividad y jurisdicción concretas.
- `REWARD_FUNDED`: fondos y reglas verificables; no basta con anunciar recompensas.

## Control algorítmico

Antes de cualquier transacción, el launcher debe comprobar: red/chain ID esperado; dirección de destino; hash de artefacto; propietario autorizado; supply máximo; URI no vacía; fondos suficientes para gas; simulación cuando la red lo permita; y confirmación explícita del firmante. Después debe guardar el hash de transacción y consultar recibo, estado, bloque, bytecode y eventos. Fallo en un control bloquea el paso siguiente.

## Regulación y límites jurisdiccionales

La clasificación depende de la función real del token y del servicio: coleccionable/obra digital, activo virtual usado como medio de pago, valor/instrumento financiero, participación, crédito, derecho sobre un bien o prestación de custodia/intercambio. No se debe declarar que un token es “legalizado”, “respaldado” o “título de propiedad” únicamente por acuñarlo.

Para México, el análisis debe partir de la Ley para Regular las Instituciones de Tecnología Financiera, especialmente artículos 30–34, de las disposiciones aplicables de Banco de México (incluida Circular 4/2019 para entidades financieras), de las obligaciones que correspondan bajo LFPIORPI cuando se realicen actividades vulnerables, y de la Ley del Mercado de Valores si el diseño puede constituir un valor. La aplicabilidad depende del servicio, habitualidad, clientes y derechos incorporados. El registro en blockchain no reemplaza permisos, obligaciones fiscales, registros inmobiliarios ni procedimientos administrativos.

Fuentes oficiales de referencia:
- Ley Fintech, DOF: https://sidof.segob.gob.mx/notas/docFuente/5515623
- Circular 4/2019, DOF: https://sidof.segob.gob.mx/notas/docFuente/5552303
- Banco de México, activos virtuales: https://www.banxico.org.mx/sistemas-de-pago/sobre-activos-virtuales-rie.html
- CNBV, normatividad Fintech: https://www.cnbv.gob.mx/SECTORES-SUPERVISADOS/Fintech/Paginas/NORMATIVIDAD-FINTECH.aspx

## Estado de ejecución

La publicación de este archivo y del código en GitHub prueba publicación documental. No prueba por sí misma compilación, ejecución del launcher, despliegue on-chain, acuñación, registro de dominio blockchain, financiación de recompensas, titularidad de bienes ni reconocimiento regulatorio. Esos estados solo se actualizan con evidencia verificable específica de cada red y acto.
