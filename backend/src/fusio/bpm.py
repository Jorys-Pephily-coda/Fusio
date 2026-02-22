import librosa

def estimate_bpm(path):
    y, sr = librosa.load(path)
    tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)
    if hasattr(tempo, "item"):
        tempo = tempo.item()
    return float(tempo)
