from pathlib import Path
import json

STATE_FILE = Path(".meeting_state.json")


def save_state(data: dict):
    STATE_FILE.write_text(json.dumps(data, indent=2))


def load_state():
    if not STATE_FILE.exists():
        return None
    return json.loads(STATE_FILE.read_text())


def clear_state():
    if STATE_FILE.exists():
        STATE_FILE.unlink()