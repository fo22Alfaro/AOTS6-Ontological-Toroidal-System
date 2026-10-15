# AOTS⁶ — Gobernanza algorítmica de criptomercados y protocolo de recuperación
**Autor:** Alfredo Jhovany Alfaro García  
**Versión:** 1.0  
**Fecha:** 2026-10-15  
**Estado:** Protocolo documental operativo; no es un contrato desplegado ni ejecuta recuperaciones automáticas.

## 1. Objetivo
Establecer un procedimiento auditable para detectar movimientos no reconocidos, preservar evidencia, clasificar permisos y tramitar recuperaciones únicamente mediante mecanismos legítimos del protocolo o del titular autorizado.

## 2. Principios de control
1. **Solo lectura primero:** obtener transacciones, recibos, logs, calldata, código/implementación y estado de permisos antes de enviar cualquier operación.
2. **No confundir direcciones:** separar dirección del titular, contrato de colección, proxy, implementación, operador/relayer, marketplace y destino receptor.
3. **Sin recuperación por suposición:** una transferencia confirmada no implica que el activo sea recuperable. No existe reversión general de transferencias confirmadas en Polygon.
4. **No firmar durante la investigación:** nunca pedir, registrar ni publicar seed phrases, claves privadas o firmas reutilizables.
5. **Doble revisión:** cualquier revocación, transferencia o llamada administrativa requiere verificar cadena, contrato, función, destinatario, gas, permisos y simulación.
6. **Evidencia reproducible:** guardar JSON crudo de recibos, calldata, logs, altura de bloque, hash de bloque, UTC de consulta, herramienta/proveedor y SHA-256 de cada archivo.
7. **Neutralidad de atribución:** describir lo que demuestran los datos; no inferir identidad, intención ni fraude como hecho probado sin evidencia adicional.

## 3. Clasificación de incidentes
- **P0 — posible drenaje activo:** movimientos nuevos no reconocidos, approvals/operator approvals inesperados, o control administrativo desconocido. Preservar datos y suspender interacciones; evaluar revocación desde una cartera segura.
- **P1 — movimientos confirmados:** transferencias de activos en cadena con recibos exitosos. Seguir token IDs, propietarios actuales, aprobaciones y llamadas internas.
- **P2 — riesgo de permisos:** operadores ERC-721/1155, allowances ERC-20, firmas EIP-712/permit, sesiones de marketplace o delegaciones.
- **P3 — activos quemados o inaccesibles:** destino cero u otra dirección sin clave conocida. No prometer recuperación; escalar solo si existe mecanismo explícito del contrato.
- **P4 — spam/metadata:** NFT no solicitados o tokens falsos. No abrir enlaces ni firmar interacciones.

## 4. Flujo de respuesta
A. **Congelar evidencia:** exportar el CSV original, guardar capturas completas y hashes de transacción; no editar los originales.  
B. **Verificar cadena:** confirmar chain ID, contrato del token, bloque y recibo.  
C. **Decodificar:** identificar selector/calldata, eventos Transfer/Approval/ApprovalForAll, logs del relayer y llamadas internas cuando el proveedor las soporte.  
D. **Reconstruir autorización:** determinar owner anterior, operator aprobado, firma/meta-transacción, nonce, deadline, relayer y función exacta. Un remitente de nivel superior distinto del owner puede ser compatible con meta-transacciones; no prueba autorización ni abuso por sí solo.  
E. **Contener:** si quedan activos bajo control del titular, moverlos a una cartera limpia solo después de revisar la seguridad; revocar approvals peligrosos desde la interfaz oficial verificada. No interactuar con contratos o enlaces enviados por terceros.  
F. **Recuperar:** solo usar función de recuperación explícita y documentada, cooperación del receptor/plataforma, o vías legales. No existe una función universal para revertir transferencias.  
G. **Publicar resultado:** separar hechos confirmados, hipótesis, datos ausentes y acciones ejecutadas.

## 5. Reglas de gobernanza de mercado
- No ejecutar trades ni liquidaciones basándose únicamente en un detector automático.
- Toda regla algorítmica debe tener versión, parámetros públicos, límites de exposición, control de slippage, protección contra replay, límites de frecuencia y botón de parada.
- Mantener segregación de funciones entre observación, propuesta, autorización y ejecución.
- Simular en fork/testnet y verificar casos negativos antes de cualquier despliegue.
- Registrar entradas, decisión, versión del modelo, autorización, hash de transacción y recibo final.
- Ningún sistema puede prometer ganancias, recuperación garantizada ni reversión de una transacción finalizada.

## 6. Hechos iniciales del caso (no conclusión jurídica)
- En el extracto recibido hay transacciones etiquetadas como `Execute Batch And Ensure Balance` y `Transfer From`.
- Los recibos consultados de dos transacciones en Polygon contienen eventos del contrato `0xa9a6a3626993d487d2dbda3173cf58ca1a9d9e9f` con movimientos ERC-721 hacia `0x7be83293BeeDc9Eba1bd76c66A65F10F3efaeC26`.
- Una consulta de almacenamiento EIP-1967 devolvió la implementación `0x11227e54f19934164a81d5add1ce5825d46b2271` para ese proxy en el estado consultado.
- En una transacción distinta, el recibo contiene un evento Transfer desde dirección cero hacia `0x2e69cbb65ce5bdc3b17df908f1480922427917e9`, y eventos de registro de dominios. Esto indica emisión/registro de un activo en esa operación, no prueba por sí solo relación con el incidente.
- Los datos compartidos no bastan para concluir quién autorizó cada operación ni si existe recuperación administrativa.

## 7. Criterios de cierre
El incidente no se marca como resuelto hasta que: (1) cada token ID esté localizado; (2) permisos y operadores estén documentados; (3) se identifique la vía de autorización; (4) las medidas de contención se hayan confirmado en cadena, si proceden; y (5) se publique un informe con hashes y recibos verificables.

## 8. Límites operativos
Este documento no ejecuta transacciones, no cambia permisos on-chain y no constituye asesoría legal. Las escrituras en GitHub preservan el protocolo documental, no bloquean por sí mismas un contrato ni recuperan activos.
