#!/data/data/com.termux/files/usr/bin/bash
set -Eeuo pipefail

ROOT="\${1:-$HOME/aots6-obom}"
cd "$ROOT"

test -f evidence/claims.ttl
test -f aots6_obom.py
command -v python >/dev/null
python aots6_obom.py verify

echo "LOCAL_A2_OBOM_VERIFY_COMPLETE"
echo "Next: export only sanitized evidence and metadata to the GitHub repository."
