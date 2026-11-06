#!/usr/bin/env python3
"""Transcribe a local audio file (e.g. a Slack voice message) with faster-whisper.

Runs fully inside the container: the audio is never sent to an external service.
The only network access is the one-time model download from Hugging Face.

Usage:
    python3 -I transcribe.py <audio_file> [--model small|medium] [--language en|auto]

Audio is decoded with ffmpeg (not PyAV) to avoid a known PyAV/faster-whisper
version incompatibility (`open() got an unexpected keyword argument 'metadata_errors'`).
"""
import argparse
import shutil
import subprocess
import sys
import time


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("audio_file")
    parser.add_argument("--model", default="small", help="Whisper model size (default: small)")
    parser.add_argument("--language", default="en", help="Language code, or 'auto' to detect (default: en)")
    args = parser.parse_args()

    if shutil.which("ffmpeg") is None:
        print("ERROR: ffmpeg is not installed.", file=sys.stderr)
        return 2
    try:
        import numpy as np
        from faster_whisper import WhisperModel
    except ImportError:
        print("ERROR: faster-whisper is not installed. Run: pip install -q faster-whisper", file=sys.stderr)
        return 2

    start = time.time()
    try:
        raw = subprocess.run(
            ["ffmpeg", "-nostdin", "-loglevel", "error", "-i", args.audio_file,
             "-f", "s16le", "-ac", "1", "-ar", "16000", "-"],
            capture_output=True, check=True,
        ).stdout
    except subprocess.CalledProcessError as exc:
        print(f"ERROR: ffmpeg could not decode the file: {exc.stderr.decode(errors='replace')}", file=sys.stderr)
        return 1
    audio = np.frombuffer(raw, np.int16).astype(np.float32) / 32768.0

    model = WhisperModel(args.model, device="cpu", compute_type="int8")
    language = None if args.language == "auto" else args.language
    segments, info = model.transcribe(audio, language=language, vad_filter=True)
    text = " ".join(seg.text.strip() for seg in segments)

    print(f"[model={args.model} language={info.language} duration={info.duration:.0f}s "
          f"elapsed={time.time() - start:.0f}s]")
    print(text if text else "[no speech detected]")
    return 0


if __name__ == "__main__":
    sys.exit(main())
