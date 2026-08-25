from pathlib import Path
from bpm import estimate_bpm
from key_finder.key import estimate_key
from key_finder.key_better import detect_key
from key_finder.key_me import find_key

# audio_path = Path(__file__).resolve().parents[3] / "data" / "input" / "bm.mp3"
audio_path = Path(__file__).resolve().parents[3] / "data" / "input" / "corn_i"
# audio_path = Path(__file__).resolve().parents[3] / "data" / "input" / "ab.mp3"


def main():
    bpm = estimate_bpm(audio_path)
    key = estimate_key(audio_path)
    key_better = detect_key(audio_path)
    key_me = find_key(audio_path)

    print(f"Estimated BPM: {bpm:.2f}")
    print(f"Estimated Key: {key}")
    print(f"Estimated Key (better): {key_better}")
    print(f"Estimated Key (me): {key_me}")


if __name__ == "__main__":
    main()
