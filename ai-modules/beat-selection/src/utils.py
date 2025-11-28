# utils.py
import logging

logging.basicConfig(level=logging.INFO)

def log_event(message: str):
    """
    Log un événement dans la console.
    """
    logging.info(message)

def normalize_features(features: dict):
    """
    Normalise les features pour les rendre comparables.
    """
    # Exemple : mise à l’échelle du tempo
    features["tempo"] = features["tempo"] / 200.0
    return features
