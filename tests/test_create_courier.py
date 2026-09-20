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
