from fastapi.testclient import TestClient
from main import app 

client = TestClient(app)

def test_root_endpoint():
    """Tests the main "/" endpoint."""
    response = client.get("/")
    
    # Check that the request was successful
    assert response.status_code == 200
    
    # Check that the response data is exactly what we expect
    assert response.json() == {
        "message": "Hello, DEVOPS!!!!!"
    }

def test_status_endpoint():
    """Tests the "/status" endpoint."""
    response = client.get("/status")
    
    assert response.status_code == 200
    assert response.json()["status"] == "200"
