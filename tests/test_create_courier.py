import allure
import requests

from data import BASE_URL, COURIER_ENDPOINT, COURIER_LOGIN_ENDPOINT


@allure.title("Создание нового курьера")
@allure.feature("Курьер")
@allure.story("Создание курьера")
def test_create_courier(courier_data, cleanup_courier):
    payload = courier_data

    response = requests.post(
        f"{BASE_URL}{COURIER_ENDPOINT}",
        json=payload
    )

    assert response.status_code == 201
    assert response.json()["ok"] is True

    login_response = requests.post(
        f"{BASE_URL}{COURIER_LOGIN_ENDPOINT}",
        json={
            "login": payload["login"],
            "password": payload["password"]
        }
    )

    assert login_response.status_code == 200

    courier_id = login_response.json()["id"]

    cleanup_courier.append(courier_id)


@allure.title("Нельзя создать курьера с уже существующим логином")
@allure.feature("Курьер")
@allure.story("Создание курьера")
def test_create_duplicate_courier(courier_data, cleanup_courier):
    payload = courier_data

    # Создаём первого курьера
    response = requests.post(
        f"{BASE_URL}{COURIER_ENDPOINT}",
        json=payload
    )

    assert response.status_code == 201
    assert response.json()["ok"] is True

    # Авторизуемся, чтобы получить id курьера
    login_response = requests.post(
        f"{BASE_URL}{COURIER_LOGIN_ENDPOINT}",
        json={
            "login": payload["login"],
            "password": payload["password"]
        }
    )

    assert login_response.status_code == 200

    courier_id = login_response.json()["id"]

    # Добавляем id в список для удаления после теста
    cleanup_courier.append(courier_id)

    # Пытаемся создать второго курьера с тем же логином
    duplicate_response = requests.post(
        f"{BASE_URL}{COURIER_ENDPOINT}",
        json=payload
    )

    assert duplicate_response.status_code == 409
    assert duplicate_response.json()["message"] == (
        "Этот логин уже используется. Попробуйте другой."
    )


@allure.title("Нельзя создать курьера без логина")
@allure.feature("Курьер")
@allure.story("Создание курьера")
def test_create_courier_without_login():
    payload = {
        "password": "password123",
        "firstName": "Test"
    }

    response = requests.post(
        f"{BASE_URL}{COURIER_ENDPOINT}",
        json=payload
    )

    assert response.status_code == 400
    assert response.json()["message"] == (
        "Недостаточно данных для создания учетной записи"
    )


@allure.title("Нельзя создать курьера без пароля")
@allure.feature("Курьер")
@allure.story("Создание курьера")
def test_create_courier_without_password():
    payload = {
        "login": "test_without_password",
        "firstName": "Test"
    }

    response = requests.post(
        f"{BASE_URL}{COURIER_ENDPOINT}",
        json=payload
    )

    assert response.status_code == 400
    assert response.json()["message"] == (
        "Недостаточно данных для создания учетной записи"
    )
    