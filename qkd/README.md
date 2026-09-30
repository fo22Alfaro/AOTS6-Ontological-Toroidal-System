# AOTS6 QKD — Interfaz interna de procedencia y custodia

Esta interfaz formaliza QKD como **desarrollo interno de AOTS6** y crea una frontera de seguridad entre el material secreto y el registro histórico público.

## Qué activa

- procedencia declarada como `AOTS6-INTERNAL-QKD`;
- identificación de autor: Alfredo Jhovany Alfaro García;
- digest SHA-256 del material recibido;
- identificador de clave y secuencia;
- sello temporal de generación suministrado por el proceso fuente;
- protección contra reatestado del mismo evento;
- verificación posterior del material contra su digest;
- registro público sin exponer la clave secreta.

## Regla fundamental

El repositorio **no contiene claves QKD secretas**. La interfaz sólo recibe material de un proceso autorizado, calcula su huella y genera una evidencia de procedencia. No fabrica fotones, claves físicas ni resultados experimentales.

Esto permite preservar la historia computacional del desarrollo sin convertir secretos operativos en evidencia pública.

## Estado epistemológico

La interfaz y su política son software verificable. La existencia de una clave generada por un proceso QKD físico requiere evidencia de ese proceso; no se infiere del digest ni del registro Git.
