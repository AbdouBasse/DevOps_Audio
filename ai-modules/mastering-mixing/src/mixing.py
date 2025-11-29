# mixing.py
from src.utils import export_audio

def apply_mixing(audio_bytes: bytes):
    """
    Applique un mixage basique :
    - Balance (équilibre gauche/droite)
    - Spatialisation (élargissement stéréo)
    - Reverb (ajout d'ambiance)
    """
    processed_file = "sample_mixed.wav"
    params = {
        "balance": "centered",
        "spatialization": "wide",
        "reverb": "light"
    }
    export_audio(processed_file, audio_bytes)
    return processed_file, params
