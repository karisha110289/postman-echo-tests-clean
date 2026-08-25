import requests

BASE_URL = "https://httpbin.org"

def test_get_simple():
    """Тест 1: простой GET — просто проверяем, что сервер ответил 200"""
    response = requests.get(f"{BASE_URL}/get")
    assert response.status_code == 200


def test_post_simple():
    """Тест 2: простой POST — отправляем данные, проверяем 200"""
    payload = {"key": "value"}
    response = requests.post(f"{BASE_URL}/post", json=payload)
    assert response.status_code == 200


def test_put_simple():
    """Тест 3: простой PUT — отправляем данные, проверяем 200"""
    payload = {"name": "test"}
    response = requests.put(f"{BASE_URL}/put", json=payload)
    assert response.status_code == 200


def test_delete_simple():
    """Тест 4: простой DELETE — просто удаляем (на httpbin это безопасно), проверяем 200"""
    response = requests.delete(f"{BASE_URL}/delete")
    assert response.status_code == 200


def test_get_with_param():
    """Тест 5: GET с параметром — передаём параметр, проверяем 200"""
    params = {"test": "123"}
    response = requests.get(f"{BASE_URL}/get", params=params)
    assert response.status_code == 200