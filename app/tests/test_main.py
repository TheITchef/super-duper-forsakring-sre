from fastapi.testclient import TestClient
from policy_api.main import app

client = TestClient(app)


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"


def test_get_policy():
    response = client.get("/policy/P001")
    assert response.status_code == 200
    assert response.json()["holder"] == "Anna Svensson"


def test_policy_not_found():
    response = client.get("/policy/INVALID")
    assert response.status_code == 404
