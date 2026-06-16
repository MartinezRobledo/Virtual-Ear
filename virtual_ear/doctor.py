import shutil
import subprocess
import tempfile
from pathlib import Path

from faster_whisper import WhisperModel
from virtual_ear.config import CONFIG


def check_ffmpeg() -> bool:
    return shutil.which("ffmpeg") is not None


def test_audio(device_name: str, label: str):
    tmp = Path(tempfile.gettempdir()) / f"{label}.wav"

    cmd = [
        "ffmpeg",
        "-y",
        "-f",
        "dshow",
        "-i",
        f"audio={device_name}",
        "-t",
        "3",
        str(tmp),
    ]

    subprocess.run(cmd, capture_output=True, text=True)

    ok = tmp.exists() and tmp.stat().st_size > 1000
    return ok, tmp


def test_whisper(wav_file: Path) -> bool:
    try:
        model = WhisperModel(
            CONFIG["whisper"]["model"],
            device="cpu",
            compute_type="int8",
        )

        segments, _ = model.transcribe(str(wav_file))

        text = "".join(s.text for s in segments).strip()

        return len(text) > 0

    except Exception:
        return False


def run():
    print("\n🩺 MEETING DOCTOR\n")

    # FFmpeg
    ffmpeg_ok = check_ffmpeg()
    print("✓ ffmpeg" if ffmpeg_ok else "✗ ffmpeg")

    if not ffmpeg_ok:
        print("\n❌ FFmpeg no disponible")
        return

    # Audio devices
    system_device = CONFIG["audio"]["system"]
    mic_device = CONFIG["audio"]["microphone"]

    system_ok, system_file = test_audio(system_device, "system_audio")
    mic_ok, mic_file = test_audio(mic_device, "mic_audio")

    print("✓ system audio" if system_ok else "✗ system audio")
    print("✓ microphone" if mic_ok else "✗ microphone")

    # Whisper (solo si hay audio válido)
    whisper_ok = False

    if system_ok:
        whisper_ok = test_whisper(system_file)

    print("✓ whisper" if whisper_ok else "✗ whisper")

    # Final
    print("\n---")

    if ffmpeg_ok and system_ok and whisper_ok:
        print("🟢 READY FOR MEETINGS")
    else:
        print("🔴 NOT READY")

        if not system_ok:
            print("- revisar captura de audio")
        if not whisper_ok:
            print("- revisar whisper / modelo")