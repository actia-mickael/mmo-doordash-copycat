import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

# --- Tests d'intégration : scénarios complets ---

def test_full_delivery_workflow():
    """Test du parcours complet : vérifier statut, calculer frais, estimer temps"""
    # 1. Vérifier que le service est up
    response = client.get("/status/")
    assert response.status_code == 200
    assert response.json()["status"] == "Service is up and running"

    # 2. Calculer les frais pour une livraison
    response = client.post("/calculate-fee/", json={"distance_km": 10, "weight_kg": 2})
    assert response.status_code == 200
    fee = response.json()["delivery_fee"]
    assert fee == 5.00 + (1.50 * 10) + (0.50 * 2)  # 21.0

    # 3. Estimer le temps de livraison
    response = client.get("/estimate-time/10")
    assert response.status_code == 200
    time = response.json()["estimated_delivery_time_minutes"]
    assert time == 10 + (5 * 10)  # 60 minutes

def test_multiple_deliveries():
    """Test de plusieurs livraisons consécutives"""
    deliveries = [
        {"distance_km": 5, "weight_kg": 1},
        {"distance_km": 15, "weight_kg": 3},
        {"distance_km": 2, "weight_kg": 0.5},
    ]
    
    for delivery in deliveries:
        response = client.post("/calculate-fee/", json=delivery)
        assert response.status_code == 200
        assert "delivery_fee" in response.json()

def test_edge_cases():
    """Test des cas limites"""
    # Distance 0
    response = client.get("/estimate-time/0")
    assert response.status_code == 200
    assert response.json()["estimated_delivery_time_minutes"] == 10

    # Très grande distance
    response = client.post("/calculate-fee/", json={"distance_km": 1000, "weight_kg": 100})
    assert response.status_code == 200
    