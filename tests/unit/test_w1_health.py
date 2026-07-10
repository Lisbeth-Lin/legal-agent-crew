import pytest
from fastapi.testclient import TestClient

from app.main import create_app


@pytest.mark.unit
def test_health_endpoint_returns_ok() -> None:
    client = TestClient(create_app())

    response = client.get("/health")

    assert response.status_code == 200
    body = response.json()
    assert body["success"] is True
    assert body["data"]["status"] == "ok"
    assert body["data"]["service"] == "PublicLaw Research Agent"
