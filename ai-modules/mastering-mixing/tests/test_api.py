# test_api.py
import pytest
from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_master_endpoint():
    """
    Vérifie que l’endpoint /master retourne bien un fichier traité.
    """
    response = client.post("/master", files={"file": b"fake_audio_bytes"})
    assert response.status_code == 200
    data = response.json()
    assert "processed_file" in data
    assert "parameters" in data

def test_mix_endpoint():
    """
    Vérifie que l’endpoint /mix retourne bien un fichier traité.
    """
    response = client.post("/mix", files={"file": b"fake_audio_bytes"})
    assert response.status_code == 200
    data = response.json()
    assert "processed_file" in data
    assert "parameters" in data
