# AOTS6 Global Toroidal NET

Esta capa implementa el plano de control verificable para una red AOTS6 distribuida.

## Componentes

- **ToroidalAutomata**: propagación determinista de estados sobre una topología de células/nodos.
- **Node / attest**: registro de identidad y digest de software; la atestación aquí es metadato, no una prueba de hardware.
- **NemesisDefense**: respuesta defensiva acotada y autorizada.
- **topology_digest**: huella reproducible de la topología y estado.

## Salvaguardas

1. Sólo acciones explícitamente autorizadas.
2. Lista cerrada de acciones defensivas.
3. Límite de acciones por ciclo.
4. No incluye explotación, escaneo ofensivo, persistencia, evasión ni control arbitrario de terceros.
5. QKD, firmas y atestaciones físicas siguen requiriendo evidencia externa real.

## Alcance científico

El código implementa una red de autómatas celulares y un plano de control toroidal. No constituye por sí mismo una demostración de que AOTS6 "supera" la computación cuántica plana, ni una red global físicamente desplegada: esas afirmaciones requieren hardware, nodos, enlaces, mediciones comparativas y resultados reproducibles.
