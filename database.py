FILE = "seen.txt"

def load_seen():
    try:
        with open(FILE, "r", encoding="utf-8") as f:
            return set(f.read().splitlines())
    except FileNotFoundError:
        return set()

def save_seen(data):
    with open(FILE, "w", encoding="utf-8") as f:
        f.write("\n".join(data))