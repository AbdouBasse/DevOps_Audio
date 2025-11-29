# test_mastering.py
import pytest
from src.mastering import apply_mastering

def test_apply_mastering_output():
    """
    Vérifie que la fonction de mastering retourne bien
    un fichier traité et des paramètres.
    """
    fake_audio = b"fake_audio_bytes"
    processed_file, params = apply_mastering(fake_audio)

    assert isinstance(processed_file, str)
    assert processed_file.endswith(".wav")
    assert "eq" in params
    assert "compression" in params
    assert "normalization" in params
