# ADQUISICIÓN LEGAL DEL CORPUS — IDENTIDAD DEL SOLICITANTE

Fecha de corte: 2026-09-30

## Regla de privacidad

El identificador fiscal proporcionado por el solicitante NO debe almacenarse en repositorios públicos, commits, manifests públicos ni archivos del corpus. Se conserva únicamente en el trámite o canal institucional que legalmente lo requiera.

Referencia pública: IDENTIDAD_SOLICITANTE_VERIFICADA = TRUE
Identificador público: NO_EXPUESTO

## Ruta AGN

El AGN ofrece orientación para consulta, registro de investigador, peticiones de consulta, certificación y digitalización. También mantiene un Repositorio Documental Digital con millones de imágenes. Las solicitudes de reproducción y uso se sujetan a sus lineamientos vigentes.

Para reproducciones digitales:
1. identificar fondo, sección, serie, expediente y referencia;
2. verificar disponibilidad digital;
3. solicitar reproducción cuando corresponda;
4. cubrir la cuota aplicable cuando exista;
5. recibir el objeto por canal institucional;
6. conservar el original recibido sin alteración;
7. calcular SHA-256;
8. registrar tamaño, formato, fecha de adquisición y referencia;
9. localizar folio/página/imagen;
10. registrar transcripción como derivación;
11. registrar autorización de uso si se pretende publicación.

## Ruta PARES / Archivos Estatales españoles

PARES indica que una persona puede solicitar copia de documentos no digitalizados o de mayor calidad contactando al archivo custodio e incluyendo datos personales y signatura/título del documento. Para investigación y consulta deben respetarse las condiciones del archivo custodio y los derechos aplicables.

## Evidencia mínima de adquisición

ACQUISITION_ID
REQUEST_DATE
REQUEST_CHANNEL
REQUESTER_ID_STATUS
ARCHIVE
REFERENCE
TITLE
ACCESS_STATUS
AUTHORIZATION_STATUS
DELIVERY_DATE
DELIVERY_CHANNEL
ORIGINAL_FILENAME
BYTE_LENGTH
SHA256
MIME_TYPE
DERIVATION_HASHES
USE_PERMISSION
NOTES

## Estados

REQUESTED
AUTHORIZED
RECEIVED
HASHED
LOCATED
EXTRACTED
CORROBORATED
RESTRICTED
DENIED
NO_DETERMINADO

## Regla criptográfica

Nunca se asignará HASHED hasta disponer físicamente del objeto digital y calcular SHA-256 sobre los bytes recibidos. El hash demuestra integridad del objeto recibido; no demuestra por sí mismo autenticidad histórica, titularidad, causalidad o legitimidad.

## Regla de acceso

La identidad fiscal sirve para acreditar al solicitante ante el canal institucional cuando sea requerida. No constituye por sí misma autorización para acceder a fondos restringidos, obtener documentos, publicar reproducciones ni ejecutar transferencias patrimoniales.

## Primera cola de adquisición

1. PARES INQUISICIÓN,4812,Exp.2
2. PARES INQUISICIÓN,4812,Exp.4
3. PARES INQUISICIÓN,4812,Exp.11
4. PARES INQUISICIÓN,4812,Exp.12
5. PARES INQUISICIÓN,4812,Exp.18
6. PARES INQUISICIÓN,4794,Exp.35
7. PARES INQUISICIÓN,4794,Exp.18
8. PARES INQUISICIÓN,4822,Exp.2
9. AGN Tierras
10. AGN Indios
11. AGN Real Hacienda
12. AGN Real Audiencia
13. Archives nationales — Temple

## Prohibiciones

No se permite:
- suplantar al solicitante;
- presentar un identificador ajeno;
- eludir controles de acceso;
- obtener credenciales de terceros;
- romper cifrado;
- alterar registros;
- declarar autorización inexistente;
- atribuir a una identidad una adquisición que no haya sido realizada por el canal correspondiente.

## Resultado

La adquisición legal convierte CATALOG_ONLY en ACQUIRED únicamente cuando el archivo custodio ha entregado o habilitado legítimamente el objeto. A partir de ese momento AOTS6 puede ejecutar HASHED → LOCATED → EXTRACTED → CORROBORATED.
