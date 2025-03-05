from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_risk_assessment():
    response = client.post("/risk_assessment/", json={"company_name": "TestCorp", "location": "New York"})
    assert response.status_code == 200
    assert "map_image_link" in response.json()
