import sys
from pathlib import Path

from pytest_asyncio import fixture

from main import app

# Add the backend directory to Python path for imports
backend_dir = Path(__file__).parent.parent
sys.path.insert(0, str(backend_dir))


@fixture
def client():
    from fastapi.testclient import TestClient

    return TestClient(app)


def test_fastapi_root(client):
    response = client.get("/api/v1/")
    assert response.status_code == 200
    assert response.json() == {"message": "ASK WISE API is running!"}


def test_fsm_endpoint(client):
    # First, POST a sample FSM
    fsm = {
        "initial_state": "OFF",
        "states": ["OFF", "ON", "ERROR"],
        "marked_states": ["OFF", "ERROR"],
        "events": ["TURN_ON", "TURN_OFF", "ERROR"],
        "transition_function": {
            "OFF:TURN_ON": "ON",
            "ON:TURN_OFF": "OFF",
            "ON:ERROR": "ERROR",
            "OFF:ERROR": "ERROR",
            "ERROR:TURN_ON": "ERROR",
            "ERROR:TURN_OFF": "ERROR",
            "ERROR:ERROR": "ERROR",
        },
    }
    post_resp = client.post("/api/v1/fsm", json=fsm)
    assert post_resp.status_code == 200
    # Now, GET the FSM
    response = client.get("/api/v1/fsm")
    assert response.status_code == 200
    data = response.json()
    assert data == fsm


def test_health_endpoint(client):
    response = client.get("/api/v1/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}
