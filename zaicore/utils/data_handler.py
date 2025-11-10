import json, os

def load_memory(path):
    if os.path.exists(path):
        try:
            with open(path, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            return {}
    return {}

def save_memory(data, path):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

def load_config():
    cfg_path = "zai_config.json"
    if os.path.exists(cfg_path):
        try:
            with open(cfg_path, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            return {}
    return {}
