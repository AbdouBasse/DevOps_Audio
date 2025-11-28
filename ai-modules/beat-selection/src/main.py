# main.py
from fastapi import FastAPI, UploadFile, File
from src.features import extract_features
from src.model import recommend_beat

app = FastAPI(title="DevOps Audio – Beat Selection")

@app.post("/analyze")
async def analyze_audio(file: UploadFile = File(...)):
    """
    Endpoint pour analyser un fichier audio.
    Retourne les features extraites (tempo, tonalité, énergie...).
    """
    features = extract_features(await file.read())
    return {"features": features}

@app.post("/recommend")
async def recommend_audio(file: UploadFile = File(...)):
    """
    Endpoint pour recommander un beat adapté.
    Utilise le modèle IA pour prédire le style le plus pertinent.
    """
    features = extract_features(await file.read())
    beat, confidence = recommend_beat(features)
    return {"recommended_beat": beat, "confidence": confidence}
