# test_model.py
import pytest
from src.model import recommend_beat

def test_recommend_beat_output():
    """
    Vérifie que la fonction retourne un beat et une confiance.
    """
    fake_features = {"tempo": 120, "rms": 0.5, "mfccs": [0.1, 0.2]}
    beat, confidence = recommend_beat(fake_features)

    assert isinstance(beat, str)
    assert isinstance(confidence, float)
    assert 0.0 <= confidence <= 1.0
