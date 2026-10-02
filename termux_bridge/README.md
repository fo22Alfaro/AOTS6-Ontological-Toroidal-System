# AOTS6 ↔ Termux bridge

Canal operativo basado en Git: **GitHub actúa como buzón**, y Termux hace polling/push.

## Activación

En Termux, con el repositorio ya clonado:

    cd "$HOME/AOTS6-Ontological-Toroidal-System"
    chmod +x termux_bridge/poll_once.sh
    termux_bridge/poll_once.sh

## Protocolo

1. Un task JSON aparece en `termux_bridge/TASK.json`.
2. Termux hace `git pull --ff-only`.
3. El agente ejecuta únicamente acciones explícitamente permitidas.
4. El resultado queda en `termux_bridge/RESULT.json`.
5. Termux hace commit + push.
6. El controlador puede leer el resultado desde GitHub.

La versión inicial permite: `status`, `hash`, `tests`.

No se ejecuta shell arbitrario recibido desde GitHub.
