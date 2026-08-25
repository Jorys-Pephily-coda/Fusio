import librosa
import numpy as np

keys = ['C', 'C#', 'D', 'D#', 'E', 'F',
        'F#', 'G', 'G#', 'A', 'A#', 'B']

def estimate_key(path):
    y, sr = librosa.load(path)

    chroma = librosa.feature.chroma_stft(y=y, sr=sr)
    chroma_mean = np.mean(chroma, axis=1)

    key_index = np.argmax(chroma_mean)

    return keys[key_index]
