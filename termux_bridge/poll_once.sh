#!/data/data/com.termux/files/usr/bin/bash
set -Eeuo pipefail
ROOT="${AOTS6_ROOT:-$HOME/AOTS6-Ontological-Toroidal-System}"
cd "$ROOT"
git pull --ff-only origin main

TASK="termux_bridge/TASK.json"
RESULT="termux_bridge/RESULT.json"

if [ ! -f "$TASK" ]; then
  echo "NO_TASK"
  exit 0
fi

python - "$TASK" "$RESULT" <<'PY'
import json,sys,subprocess,hashlib,os,time
task_path,result_path=sys.argv[1:]
task=json.load(open(task_path,encoding="utf-8"))
action=task.get("action")
allowed={"status","hash","tests"}
if action not in allowed:
    raise SystemExit(f"BLOCKED_ACTION:{action}")

root=os.getcwd()
if action=="status":
    p=subprocess.run(["git","status","--short"],capture_output=True,text=True)
    data={"action":action,"returncode":p.returncode,"stdout":p.stdout,"stderr":p.stderr}
elif action=="hash":
    targets=["README.md","AOTS6_INTEGRITY.hash","AOTS6_NET_AUTH.sig"]
    hashes={}
    for f in targets:
        if os.path.isfile(f):
            h=hashlib.sha256(open(f,"rb").read()).hexdigest()
            hashes[f]=h
    data={"action":action,"hashes":hashes}
else:
    p=subprocess.run(["python","-m","pytest","-q"],capture_output=True,text=True)
    data={"action":action,"returncode":p.returncode,"stdout":p.stdout[-12000:],"stderr":p.stderr[-12000:]}

result={"task_id":task.get("task_id"),"completed_at":time.strftime("%Y-%m-%dT%H:%M:%SZ",time.gmtime()),"host":os.uname().nodename,"python":subprocess.run(["python","--version"],capture_output=True,text=True).stderr.strip() or subprocess.run(["python","--version"],capture_output=True,text=True).stdout.strip(),"result":data}
with open(result_path,"w",encoding="utf-8") as f: json.dump(result,f,ensure_ascii=False,indent=2)
PY

git add "$RESULT"
git commit -m "Termux bridge: publish task result" || true
git push origin main
echo "AOTS6_TERMUX_BRIDGE_TASK_COMPLETE"
