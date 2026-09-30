# PROTOCOLO DE RECUPERACION LITERAL DE EVIDENCIA

## Cadena

FUENTE -> ADQUISICION -> OBJETO ORIGINAL -> SHA-256 -> LOCALIZADOR -> EXTRACCION LITERAL -> AFIRMACION

La afirmacion no puede exceder lo que dice literalmente el objeto.

## Estados

- CATALOG_ONLY: solo existe registro archivistico.
- ACQUIRED: objeto digital obtenido por acceso permitido.
- HASHED: SHA-256 calculado sobre los bytes del objeto.
- LOCATED: folio, pagina o imagen identificados.
- EXTRACTED: transcripcion literal conservada.
- CORROBORATED: fuente independiente confirma el mismo hecho.

## Regla de literalidad

Conservar texto original, idioma, pagina/folio/imagen, fecha de captura, metodo de
transcripcion y hash. El OCR es una derivacion y no sustituye la imagen original.

## Recuperacion distribuida

Buscar en archivo custodio, biblioteca o repositorio institucional, catalogos archivisticos,
copias digitales institucionales y publicaciones que reproduzcan el documento. Registrar
cada ruta y no confundir una descripcion de catalogo con el objeto primario.

## Integridad

SHA-256 demuestra correspondencia entre los bytes examinados y el hash registrado.
No demuestra por si mismo verdad historica, propiedad, autoria, causalidad o titularidad.

## Acceso

Solo se incorporan materiales disponibles mediante acceso permitido. No se evaden controles
ni se obtienen credenciales o claves ajenas.

## Regla automatica

Una entrada marcada REPRODUCIBLE debe tener SHA-256 real y, cuando el objeto esta disponible
localmente, el verificador debe recalcularlo y compararlo. Una entrada CATALOG_ONLY o
PARCIALMENTE_REPRODUCIBLE conserva explicitamente la ausencia del objeto capturado.
