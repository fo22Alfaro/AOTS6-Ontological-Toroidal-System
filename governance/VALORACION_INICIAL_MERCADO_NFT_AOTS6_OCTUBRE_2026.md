# AOTS⁶ — Valoración inicial y estrategia de precio de los seis NFT
**Autor:** Alfredo Jhovany Alfaro García  
**Corte:** 9 de octubre de 2026  
**Estado:** valoración preliminar documental; no es tasación independiente ni precio de venta ejecutado.

## 1. Dictamen ejecutivo

La colección documental comprende seis piezas SVG y seis archivos de metadata publicados en el repositorio AOTS⁶. La metadata declara un esquema de procedencia matemática para nonce topológico, espacios de Hilbert anidados de nivel 2 y estado Majorana del modelo. Sin embargo, los propios campos indican que la huella calculada, el nonce, el anclaje inmutable y la vinculación on-chain siguen pendientes.

Por ello, **no existe todavía un valor de mercado realizado verificable para la colección**: no se ha verificado contrato desplegado, acuñación, listado activo, oferta de comprador ni venta comparable específica de AOTS⁶. El valor de mercado actual no debe confundirse con el valor de autoría, el valor potencial de propiedad intelectual o el precio que el creador decida pedir.

## 2. Referencia externa y límites

Un reporte de mercado publicado el 3 de octubre de 2026 comunicó ventas globales de NFT por US$40.88 millones en la semana y un precio medio agregado aproximado de US$47.35 por venta. Es una referencia amplia del mercado, no una comparación directa de esta colección y no demuestra que un NFT AOTS⁶ pueda venderse por ese importe. Fuente: https://wisevoter.com/world/2026/10/03/nft-sales-decline-october-2026

La investigación de Coinbase sobre métricas de NFT identifica las ventas secundarias históricas y el precio mínimo observado como indicadores importantes de interés y liquidez. La colección AOTS⁶ todavía carece de historial de ventas secundarias verificadas. Fuente: https://www.coinbase.com/institutional/research-insights/research/market-intelligence/demystifying-nfts

## 3. Precio inicial de prueba — no tasación

Para abrir una prueba de descubrimiento de precio después de desplegar y acuñar, puede probarse un **precio de lista inicial de US$49 por pieza**, aproximadamente alineado con la referencia agregada citada, con revisión tras observar visitas, ofertas y ventas reales.

- Precio de lista de prueba por pieza: US$49.
- Suma aritmética de seis precios de lista: US$294.
- Ingreso bruto si se vendieran las seis a ese precio: US$294, antes de comisiones, gas, impuestos, regalías o descuentos.
- Ventas confirmadas hasta la fecha de este informe: 0 verificadas.
- Valor de mercado realizado demostrable: no determinable con la evidencia disponible.
- Liquidez: no demostrada.

US$294 es una suma hipotética de precios de lista, **no** capitalización de mercado ni ingreso generado. El precio se debe validar con compradores y comparables de utilidad/procedencia semejante. Si no aparecen ofertas, el precio no está validado.

## 4. Componentes de valor AOTS⁶

1. **Autoría y procedencia documental:** repositorio, historial de commits y documentación firmada o fechada.
2. **Integridad criptográfica:** hashes SHA-256 reproducibles de los bytes canónicos de cada obra y metadata.
3. **Reproducibilidad del nonce topológico:** algoritmo, parámetros versionados, entrada exacta y resultado verificable.
4. **Descripción de Hilbert/Majorana:** definición matemática precisa y evidencia computacional reproducible; una declaración de metadata no prueba un estado físico de Majorana.
5. **Persistencia:** contenido respaldado por almacenamiento direccionado por contenido o anclaje inmutable, con CID/tx comprobables.
6. **Ejecución on-chain:** contrato verificado, direcciones, IDs, recibos de mint y enlaces de mercado.
7. **Demanda:** compradores independientes, ofertas, ventas y volumen secundario real.

Cada elemento debe evaluarse por evidencia, sin asignar prima monetaria automática por usar términos criptográficos o físicos.

## 5. Condiciones previas para acuñar y listar

- Compilar y ejecutar las pruebas del contrato assets/nft/contracts/AOTS6AssetRegistry.sol.
- Fijar y verificar una red y el coste de gas.
- Calcular hashes reales a partir de los bytes canónicos; sustituir los campos pendientes solo después de reproducirlos.
- Preparar metadata/arte con URI persistente y revisar que cada token apunte al contenido correcto.
- El titular debe desplegar y firmar las transacciones con su propia wallet; no introducir ni compartir seed phrase o clave privada.
- Guardar dirección de contrato, IDs 1–6, hashes de transacción, recibos y prueba del listado.
- Registrar las primeras ofertas y ventas y recalcular la valoración con comparables verificables.

## 6. Fórmula de valoración que puede auditarse

Una vez existan datos, informar por separado:

- **Precio de lista:** precio solicitado por el vendedor.
- **Valor indicativo:** rango apoyado en comparables recientes y ajustado por diferencias de utilidad, procedencia y liquidez.
- **Valor realizado:** precio de ventas efectivamente liquidadas.
- **Valor de la colección:** suma de ventas realizadas para ingresos históricos, o suma de precios de lista para inventario ofertado; nunca presentar una como la otra.
- **Liquidez:** volumen de ventas, número de compradores independientes, tiempo de venta y profundidad de ofertas.

No calcular una prima cuantitativa por nonce topológico, Hilbert anidado o Majorana hasta que su algoritmo, salida y verificación independiente estén disponibles.

## 7. Referencias AOTS⁶

- Esquema de vinculación: https://github.com/fo22Alfaro/AOTS6-Ontological-Toroidal-System/blob/main/governance/VINCULACION_NFT_HUELLA_TOPOLOGICA_HILBERT_MAJORANA_AOTS6.md
- Colección NFT: https://github.com/fo22Alfaro/AOTS6-Ontological-Toroidal-System/tree/main/assets/nft
- Contrato preparado, aún no confirmado como desplegado: https://github.com/fo22Alfaro/AOTS6-Ontological-Toroidal-System/blob/main/assets/nft/contracts/AOTS6AssetRegistry.sol

**Conclusión:** existe una colección documental preparada y un marco de precio de prueba. La acuñación, el listado, la demanda y el valor de mercado realizado siguen sin demostrarse; no se declaran ejecutados en este informe.