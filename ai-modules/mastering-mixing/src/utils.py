# utils.py
import logging

logging.basicConfig(level=logging.INFO)

def log_event(message: str):
    """
    Log un événement dans la console.
    """
    logging.info(message)

def export_audio(filename: str, audio_bytes: bytes):
    """
    Simule l’export d’un fichier audio traité.
    Dans une vraie version, on écrirait les bytes sur disque.
    """
    log_event(f"Export audio -> {filename}")
    # Ici on simule l’écriture
    return True
