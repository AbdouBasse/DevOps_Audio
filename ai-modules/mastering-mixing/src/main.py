# main.py
from fastapi import FastAPI, UploadFile, File
from src.mastering import apply_mastering
from src.mixing import apply_mixing

app = FastAPI(title="DevOps Audio – Mastering & Mixing")

@app.post("/master")
async def master_audio(file: UploadFile = File(...)):
    """
    Endpoint pour appliquer un mastering sur un fichier audio.
    Retourne un fichier traité avec EQ, compression et normalisation.
    """
    audio_bytes = await file.read()
    processed_file, params = apply_mastering(audio_bytes)
    return {"status": "success", "processed_file": processed_file, "parameters": params}

@app.post("/mix")
async def mix_audio(file: UploadFile = File(...)):
    """
    Endpoint pour appliquer un mixage sur un fichier audio.
    Retourne un fichier traité avec balance, spatialisation et reverb.
    """
    audio_bytes = await file.read()
    processed_file, params = apply_mixing(audio_bytes)
    return {"status": "success", "processed_file": processed_file, "parameters": params}
