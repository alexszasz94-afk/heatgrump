"""Utilitare comune: config, .env, căi, JSON."""
import json, os, pathlib, datetime

ROOT = pathlib.Path(__file__).resolve().parent.parent
LIB, STATE, OUT, INBOX = ROOT / "library", ROOT / "state", ROOT / "output", ROOT / "inbox"

def load_env():
    p = ROOT / ".env"
    if p.exists():
        for line in p.read_text().splitlines():
            line = line.split("#", 1)[0].strip()
            if "=" in line:
                k, v = line.split("=", 1)
                os.environ.setdefault(k.strip(), v.strip())

def cfg():
    import yaml  # pip install pyyaml
    return yaml.safe_load((ROOT / "engine/config.yaml").read_text())

def jload(path, default):
    p = pathlib.Path(path)
    return json.loads(p.read_text()) if p.exists() else default

def jsave(path, obj):
    p = pathlib.Path(path); p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(obj, indent=1, ensure_ascii=False))

def today():
    return datetime.date.today().isoformat()

def log(msg):
    print(f"[{datetime.datetime.now().strftime('%H:%M:%S')}] {msg}")
