import json
import os

FILE = "seen.json"

def load_seen():
    if not os.path.exists(FILE):
        return set()

    with open(FILE, "r", encoding="utf-8") as f:
        try:
            data = json.load(f)
            return set(data)
        except:
            return set()

def save_seen(seen):
    with open(FILE, "w", encoding="utf-8") as f:
        json.dump(list(seen), f, ensure_ascii=False, indent=2)