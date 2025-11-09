import json
import os


def load_memory(path):
    """Load memory file if exists, else return new blank memory."""
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}


def save_memory(data, path):
    """Save current memory data to file."""
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)
