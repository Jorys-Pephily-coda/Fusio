import librosa
import numpy as np

KEY_NAMES = ['C','C#','D','D#','E','F',
             'F#','G','G#','A','A#','B']

MAJOR_PROFILE = np.array([
    5, 2, 3.5, 2, 4.5, 4,
    2, 4.5, 2, 3.5, 1.5, 4
])

MINOR_PROFILE = np.array([
    5, 2, 3.5, 4.5, 2, 4,
    2, 4.5, 3.5, 2, 1.5, 4
])

def pearson_correlation(x, y):
    print(np.corrcoef(x,y)[1,0])
    return np.corrcoef(x, y)[0, 1]

def rotate_profile(profile, n):
    return np.roll(profile, n)

def find_key(audio_path):
    y, sr = librosa.load(audio_path, mono=True)
    best_score = -np.inf # valeur la plus basse
    best_key = None

    # Chroma plus stable pour tonalité
    chroma = librosa.feature.chroma_cqt(
        y=y,
        sr=sr,
        bins_per_octave=36
    )


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
