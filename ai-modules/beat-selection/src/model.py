# model.py
import random

# Exemple simplifié : dans la vraie version, on chargerait un modèle entraîné
BEATS = ["Afro", "Trap", "BoomBap", "House", "Jazz"]

def recommend_beat(features: dict):
    """
    Recommande un beat en fonction des features extraites.
    Ici, on simule avec une sélection aléatoire.
    """
    beat = random.choice(BEATS)
    confidence = round(random.uniform(0.7, 0.95), 2)
    return beat, confidence
