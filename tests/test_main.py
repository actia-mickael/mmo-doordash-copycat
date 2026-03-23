import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

# --- Test connexion API ---
def test_api_connection():
    response = client.get("/")
    assert response.status_code == 200

# --- Test format données entrées ---
def test_calculate_fee_invalid_input():
    # Données manquantes
    response = client.post("/calculate-fee/", json={})
    assert response.status_code == 422

    # Mauvais type de données
    response = client.post("/calculate-fee/", json={"distance_km": "abc", "weight_kg": 2})
    assert response.status_code == 422

# --- Test format de sortie ---
def test_root_response_format():
    response = client.get("/")
    data = response.json()
    assert "message" in data
    assert isinstance(data["message"], str)

def test_calculate_fee_response_format():
    response = client.post("/calculate-fee/", json={"distance_km": 10, "weight_kg": 2})
    data = response.json()
    assert "delivery_fee" in data
    assert isinstance(data["delivery_fee"], (int, float))

def test_estimate_time_response_format():
    response = client.get("/estimate-time/5")
    data = response.json()
    assert "estimated_delivery_time_minutes" in data
    assert isinstance(data["estimated_delivery_time_minutes"], (int, float))

def test_status_response_format():
    response = client.get("/status/")
    data = response.json()
    assert "status" in data