from pathlib import Path
import os

if os.name == "nt":
    cuda_bin = (
        r"C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.9\bin"
    )
    if os.path.exists(cuda_bin):
        os.add_dll_directory(cuda_bin)

from faster_whisper import WhisperModel

from virtual_ear.config import (
    CONFIG,
    TRANSCRIPTS_DIR,
)

from faster_whisper import WhisperModel


def load_model(config: dict) -> WhisperModel:
    model_name = config["whisper"]["model"]
    device = config["whisper"]["device"]

    if device == "cpu":
        return WhisperModel(
            model_name,
            device="cpu",
            compute_type="int8",
        )

    if device == "cuda":
        return WhisperModel(
            model_name,
            device="cuda",
            compute_type="float16",
        )

    if device == "auto":
        try:
            return WhisperModel(
                model_name,
                device="cuda",
                compute_type="float16",
            )
        except Exception:
            return WhisperModel(
                model_name,
                device="cpu",
                compute_type="int8",
            )

    raise ValueError(
        f"Invalid whisper device: {device}. "
        "Expected: cpu, cuda or auto"
    )


def transcribe(wav_file):
    try:
        MODEL = load_model(CONFIG)

        segments, _ = MODEL.transcribe(
            wav_file
        )

        output = (
            TRANSCRIPTS_DIR /
            (Path(wav_file).stem + ".md")
        )

        with open(
            output,
            "w",
            encoding="utf-8",
        ) as f:
            for segment in segments:
                f.write(
                    segment.text.strip()
                )
                f.write("\n")

        return output
    except Exception as e:
        if "cublas64_12.dll" in str(e):
                raise RuntimeError(
                    "CUDA runtime not found. Install CUDA Toolkit 12.x or change whisper.device to 'cpu'."
                ) from e
        else:
            raise RuntimeError(
                    f"Failed to initialize Whisper: {e}"
                ) from e