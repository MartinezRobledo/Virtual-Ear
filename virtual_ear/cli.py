import os
import signal
import sys
import platform
import subprocess

from virtual_ear.doctor import run as doctor
from virtual_ear.state import clear_state, load_state
from virtual_ear.config import CONFIG
from virtual_ear.recorder import (
    start,
)
from virtual_ear.transcriber import (
    transcribe,
)

def kill(pid: int):
    if platform.system() == "Windows":
        subprocess.run(["taskkill", "/PID", str(pid), "/F", "/T"])
    else:
        os.kill(pid, signal.SIGTERM)


def stop():
    state = load_state()

    if not state:
        print("❌ No active recording")
        return

    pid = state["pid"]
    file = state["file"]

    print("🛑 Stopping recording...")

    kill(int(pid))

    print(f"✓ Saved: {file}")
    clear_state()

    return file


def main():
    audio = CONFIG["audio"]
    command = sys.argv[1]
    wav_file = sys.argv[2]

    if command == "doctor":
        doctor()

    elif command == "start":
        start(audio.get("system"))

    elif command == "stop":
        stop()

    elif command == "transcribe":
        transcribe(wav_file)

    else:
        raise SystemExit(
            f"Comando inválido: {command}"
        )