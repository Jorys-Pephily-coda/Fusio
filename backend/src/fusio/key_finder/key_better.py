import librosa
import numpy as np

MAJOR_PROFILE = np.array([
    6.35, 2.23, 3.48, 2.33, 4.38, 4.09,
    2.52, 5.19, 2.39, 3.66, 2.29, 2.88
])

MINOR_PROFILE = np.array([
    6.33, 2.68, 3.52, 5.38, 2.60, 3.53,
    2.54, 4.75, 3.98, 2.69, 3.34, 3.17
])

def rotate_profile(profile, n):
    return np.roll(profile, n)

def correlation(x, y):
    return np.corrcoef(x, y)[0, 1]

KEY_NAMES = ['C','C#','D','D#','E','F',
             'F#','G','G#','A','A#','B']

def detect_key(audio_path):

    y, sr = librosa.load(audio_path, mono=True)

    # Chroma plus stable pour tonalité
    chroma = librosa.feature.chroma_cqt(
        y=y,
        sr=sr,
        bins_per_octave=36
    )

    # Moyenne temporelle
    chroma_mean = np.mean(chroma, axis=1)

    # Normalisation (important)
    chroma_mean = chroma_mean / np.linalg.norm(chroma_mean)

    best_score = -np.inf
    best_key = None

    for i in range(12):

        maj_profile = rotate_profile(MAJOR_PROFILE, i)
        min_profile = rotate_profile(MINOR_PROFILE, i)

        score_maj = correlation(chroma_mean, maj_profile)
        score_min = correlation(chroma_mean, min_profile)

        if score_maj > best_score:
            best_score = score_maj
            best_key = f"{KEY_NAMES[i]} major"

        if score_min > best_score:
            best_score = score_min
            best_key = f"{KEY_NAMES[i]} minor"

    return best_key, best_score
