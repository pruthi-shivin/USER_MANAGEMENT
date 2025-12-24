from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_user():
    response = client.post("/users", json={
        "name": "Shivin",
        "email": "shivin@gmail.com",
        "primary_mobile": "9999999999",
        "secondary_mobile": "8888888888",
        "aadhaar": "123456789012",
        "pan": "ABCDE1234F",
        "date_of_birth": "2002-05-10",
        "place_of_birth": "Delhi",
        "current_address": "Delhi",
        "permanent_address": "Delhi"
    })
    assert response.status_code == 200
    assert response.json()["email"] == "shivin@gmail.com"


def test_duplicate_email():
    response = client.post("/users", json={
        "name": "Test",
        "email": "shivin@gmail.com",
        "primary_mobile": "9999999998",
        "aadhaar": "123456789013",
        "pan": "ABCDE1234G",
        "date_of_birth": "2002-05-10",
        "place_of_birth": "Delhi",
        "current_address": "Delhi",
        "permanent_address": "Delhi"
    })
    assert response.status_code == 400


def test_get_user_not_found():
    response = client.get("/users/999")
    assert response.status_code == 404


def test_pagination():
    response = client.get("/users?page=1&limit=1")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_update_user():
    response = client.post("/users", json={
        "name": "Original Name",
        "email": "update_test@gmail.com",
        "primary_mobile": "9999999997",
        "secondary_mobile": "8888888887",
        "aadhaar": "123456789014",
        "pan": "ABCDE1234H",
        "date_of_birth": "2002-05-10",
        "place_of_birth": "Delhi",
        "current_address": "Delhi",
        "permanent_address": "Delhi"
    })
    assert response.status_code == 200
    user_id = response.json()["id"]
    
    response = client.put(f"/users/{user_id}", json={
        "name": "Updated Name",
        "primary_mobile": "9999999996"
    })
    assert response.status_code == 200
    assert response.json()["name"] == "Updated Name"
    assert response.json()["primary_mobile"] == "9999999996"
    assert response.json()["email"] == "update_test@gmail.com"


def test_update_user_duplicate_email():
    client.post("/users", json={
        "name": "User One",
        "email": "user1@gmail.com",
        "primary_mobile": "9999999995",
        "aadhaar": "123456789015",
        "pan": "ABCDE1234I",
        "date_of_birth": "2002-05-10",
        "place_of_birth": "Delhi",
        "current_address": "Delhi",
        "permanent_address": "Delhi"
    })
    
    response = client.post("/users", json={
        "name": "User Two",
        "email": "user2@gmail.com",
        "primary_mobile": "9999999994",
        "aadhaar": "123456789016",
        "pan": "ABCDE1234J",
        "date_of_birth": "2002-05-10",
        "place_of_birth": "Delhi",
        "current_address": "Delhi",
        "permanent_address": "Delhi"
    })
    user_id = response.json()["id"]
    
    response = client.put(f"/users/{user_id}", json={
        "email": "user1@gmail.com"
    })
    assert response.status_code == 400