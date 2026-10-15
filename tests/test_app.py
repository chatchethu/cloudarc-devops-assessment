from app import app


def test_home_returns_success():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert response.json["application"] == "CloudArc DevOps Demo"
    assert response.json["status"] == "running"


def test_health_returns_healthy():
    client = app.test_client()
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json == {"status": "healthy"}
