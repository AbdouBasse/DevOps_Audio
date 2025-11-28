# model.py
from src.prepare_data import load_dataset
import random

BEATS = ["Afro", "Trap", "BoomBap", "House", "Jazz"]

def train_model():
    """
    Entraîne le modèle IA avec les datasets audio.
    - Charge les données via prepare_data.py
    - Associe features (X) et labels (y)
    - Simule un entraînement (dans la vraie version : PyTorch/TensorFlow)
    """
    X, y = load_dataset()
    print(f"Nombre d'échantillons chargés : {len(X)}")
    print(f"Genres disponibles : {set(y)}")
    # Ici, tu pourrais ajouter un vrai entraînement avec PyTorch/TensorFlow
    return "Modèle entraîné (simulation)"

def recommend_beat(features: dict):
    """
    Recommande un beat en fonction des features extraites.
    Pour l’instant, sélection aléatoire simulée.
    """
    beat = random.choice(BEATS)
    confidence = round(random.uniform(0.7, 0.95), 2)
    return beat, confidence
