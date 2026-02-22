from pathlib import Path
from bpm import estimate_bpm
from key import estimate_key

audio_path = Path(__file__).resolve().parents[3] / "data" / "input" / "bm.mp3"

def main():
    bpm = estimate_bpm(audio_path)
    key = estimate_key(audio_path)

    print(f"Estimated BPM: {bpm:.2f}")
    print(f"Estimated Key: {key}")

if __name__ == "__main__":
    main()
