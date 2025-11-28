# test_features.py
import pytest
from src.features import extract_features

def test_extract_features_structure():
    """
    Vérifie que la fonction retourne bien un dictionnaire
    avec les clés attendues.
    """
    # Simuler un fichier audio en bytes (ici un mock simplifié)
    fake_audio = b"fake_audio_bytes"
    features = extract_features(fake_audio)

    assert isinstance(features, dict)
    assert "tempo" in features
    assert "rms" in features
    assert "mfccs" in features

def test_extract_features_values():
    """
    Vérifie que les valeurs extraites sont numériques et cohérentes.
    """
    fake_audio = b"fake_audio_bytes"
    features = extract_features(fake_audio)

    assert isinstance(features["tempo"], float)
    assert isinstance(features["rms"], float)
    assert isinstance(features["mfccs"], list)
