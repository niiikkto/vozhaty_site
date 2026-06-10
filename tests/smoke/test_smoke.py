import requests
import pytest

BASE_URL = "http://localhost:8000"

def test_homepage():
    response = requests.get(f"{BASE_URL}/")
    assert response.status_code == 200
    # Проверяем, что на главной есть слово "материал" или "вожатка"
    assert "вожат" in response.text.lower()

def test_materials_exist_on_homepage():
    response = requests.get(f"{BASE_URL}/")
    assert response.status_code == 200
    # Проверяем, что на главной есть блок с материалами
    # (по классу или по тексту)
    assert "материал" in response.text.lower() or "материалы" in response.text.lower()

def test_gallery_exists_on_homepage():
    response = requests.get(f"{BASE_URL}/")
    assert response.status_code == 200
    # Проверяем наличие галереи на главной
    assert "галере" in response.text.lower() or "фото" in response.text.lower()

def test_admin_login_redirect():
    response = requests.get(f"{BASE_URL}/admin/", allow_redirects=False)
    assert response.status_code == 302

def test_404_page():
    response = requests.get(f"{BASE_URL}/non-existent-page/")
    assert response.status_code == 404