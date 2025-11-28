# features.py
import librosa
import numpy as np

def extract_features(audio_bytes: bytes):
    """
    Transforme un fichier audio en features exploitables par l'IA.
    - Tempo
    - Tonalité
    - Énergie (RMS)
    - MFCCs
    """
    # Charger l'audio depuis les bytes
    y, sr = librosa.load(librosa.util.buf_to_float(audio_bytes), sr=None)

    tempo, _ = librosa.beat.beat_track(y=y, sr=sr)
    rms = np.mean(librosa.feature.rms(y=y))
    mfccs = np.mean(librosa.feature.mfcc(y=y, sr=sr), axis=1)

    return {
        "tempo": float(tempo),
        "rms": float(rms),
        "mfccs": mfccs.tolist()
    }
