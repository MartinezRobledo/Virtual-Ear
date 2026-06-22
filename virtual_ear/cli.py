import io
import os
import signal
import sys
import platform
import subprocess

if platform.system() == "Windows":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8")

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
    command = sys.argv[1] if len(sys.argv) > 1 else None

    if command == "doctor":
        doctor()

    elif command == "start":
        start(audio.get("system"))

    elif command == "stop":
        stop()

    elif command == "transcribe":
        if len(sys.argv) < 3:
            raise SystemExit("Uso: earing transcribe <archivo.wav>")
        transcribe(sys.argv[2])

    else:
        raise SystemExit(
            f"Comando inválido: {command}"
        )