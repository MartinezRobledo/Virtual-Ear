from pathlib import Path
import json

ROOT = Path(__file__).resolve().parent.parent

CONFIG_FILE = ROOT / "config.json"

RECORDINGS_DIR = ROOT / "recordings"
TRANSCRIPTS_DIR = ROOT / "transcripts"
SUMMARIES_DIR = ROOT / "summaries"
STATE_DIR = ROOT / "state"

for directory in (
    RECORDINGS_DIR,
    TRANSCRIPTS_DIR,
    SUMMARIES_DIR,
    STATE_DIR,
):
    directory.mkdir(exist_ok=True)

CONFIG = json.loads(
    CONFIG_FILE.read_text(encoding="utf-8")
)