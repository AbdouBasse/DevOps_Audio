# test_mixing.py
import pytest
from src.mixing import apply_mixing

def test_apply_mixing_output():
    """
    Vérifie que la fonction de mixage retourne bien
    un fichier traité et des paramètres.
    """
    fake_audio = b"fake_audio_bytes"
    processed_file, params = apply_mixing(fake_audio)

    assert isinstance(processed_file, str)
    assert processed_file.endswith(".wav")
    assert "balance" in params
    assert "spatialization" in params
    assert "reverb" in params
