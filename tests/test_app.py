import pytest
from app.main import app, calculate_factorial, is_palindrome


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_home(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.json["version"] == "1.0.0"


def test_health(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json["status"] == "ok"


def test_create_todo(client):
    response = client.post("/todos", json={"title": "Test task"})
    assert response.status_code == 201
    assert response.json["title"] == "Test task"
    assert response.json["completed"] is False


def test_create_todo_missing_title(client):
    response = client.post("/todos", json={})
    assert response.status_code == 400


def test_get_todos(client):
    client.post("/todos", json={"title": "Task 1"})
    response = client.get("/todos")
    assert response.status_code == 200
    assert isinstance(response.json, list)


def test_math_add(client):
    response = client.get("/math/add?a=3&b=5")
    assert response.status_code == 200
    assert response.json["result"] == 8.0


def test_math_multiply(client):
    response = client.get("/math/multiply?a=4&b=6")
    assert response.status_code == 200
    assert response.json["result"] == 24.0


def test_math_add_missing_params(client):
    response = client.get("/math/add")
    assert response.status_code == 400


def test_factorial():
    assert calculate_factorial(0) == 1
    assert calculate_factorial(5) == 120
    assert calculate_factorial(10) == 3628800


def test_factorial_negative():
    with pytest.raises(ValueError):
        calculate_factorial(-1)


def test_palindrome():
    assert is_palindrome("racecar") is True
    assert is_palindrome("hello") is False
    assert is_palindrome("A man a plan a canal Panama") is True


def test_factorial_endpoint(client):
    response = client.get("/utils/factorial/5")
    assert response.status_code == 200
    assert response.json["result"] == 120


def test_palindrome_endpoint(client):
    response = client.get("/utils/palindrome?text=racecar")
    assert response.status_code == 200
    assert response.json["is_palindrome"] is True
