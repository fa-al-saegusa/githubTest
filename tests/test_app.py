import pytest
from fastapi.testclient import TestClient
from src.app import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    # Add more assertions based on your root endpoint

# Add more tests for other endpoints as needed
