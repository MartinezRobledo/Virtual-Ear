import subprocess
from pathlib import Path
from datetime import datetime

from virtual_ear.state import save_state


def start(device: str, output_dir="recordings"):
    Path(output_dir).mkdir(exist_ok=True)

    file = Path(output_dir) / f"meeting_{datetime.now().strftime('%Y%m%d_%H%M%S')}.wav"

    cmd = [
        "ffmpeg",
        "-y",
        "-f", "dshow",
        "-i", f"audio={device}",
        str(file),
    ]

    proc = subprocess.Popen(
        cmd,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )

    save_state({
        "pid": proc.pid,
        "file": str(file),
        "device": device
    })

    print("🎙️ Recording started")
    print("→ run: earing stop")