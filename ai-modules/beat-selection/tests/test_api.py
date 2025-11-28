# test_api.py
import pytest
from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_analyze_endpoint():
    """
    Vérifie que l’endpoint /analyze retourne bien des features.
    """
    response = client.post("/analyze", files={"file": b"fake_audio_bytes"})
    assert response.status_code == 200
    data = response.json()
    assert "features" in data

def test_recommend_endpoint():
    """
    Vérifie que l’endpoint /recommend retourne une recommandation.
    """
    response = client.post("/recommend", files={"file": b"fake_audio_bytes"})
    assert response.status_code == 200
    data = response.json()
    assert "recommended_beat" in data
    assert "confidence" in data
