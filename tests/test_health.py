from fastapi.testclient import TestClient

from services.api.app.main import create_app


def test_liveness_is_available_without_external_services():
    with TestClient(create_app()) as client:
        response = client.get("/api/v1/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_openapi_exposes_versioned_health_endpoint():
    with TestClient(create_app()) as client:
        response = client.get("/openapi.json")

    assert response.status_code == 200
    schema = response.json()
    assert schema["info"]["title"] == "Scalable Ticket Booking System"
    assert "200" in schema["paths"]["/api/v1/health"]["get"]["responses"]
