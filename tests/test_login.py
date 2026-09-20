import allure
import requests

from data import BASE_URL, COURIER_LOGIN_ENDPOINT

@allure.feature("Курьер")
@allure.story("Авторизация курьера")
class TestCourierLogin:
    @allure.title("Успешная авторизация курьера")
    def test_login_success(self, courier):
        payload, courier_id = courier

        response = requests.post(
            f"{BASE_URL}{COURIER_LOGIN_ENDPOINT}",
            json=payload
        )

        assert response.status_code == 200
        assert "id" in response.json()
        assert response.json()["id"] == courier_id

    def test_login_wrong_password(self, courier):
        payload, _ = courier

        payload["password"] = "wrong_password"

        response = requests.post(
            f"{BASE_URL}{COURIER_LOGIN_ENDPOINT}",
            json=payload
        )

        assert response.status_code == 404
        assert response.json()["message"] == "Учетная запись не найдена"

    def test_login_wrong_login(self, courier):
        payload, _ = courier

        payload["login"] = "wrong_login"

        response = requests.post(
            f"{BASE_URL}{COURIER_LOGIN_ENDPOINT}",
            json=payload
        )

        assert response.status_code == 404
        assert response.json()["message"] == "Учетная запись не найдена"

    def test_login_without_login(self, courier):
        payload, _ = courier

        payload.pop("login")

        response = requests.post(
            f"{BASE_URL}{COURIER_LOGIN_ENDPOINT}",
            json=payload
        )

        assert response.status_code == 400
        assert response.json()["message"] == "Недостаточно данных для входа"

    # def test_login_without_password(self, courier):
    #     payload, _ = courier

    #     payload.pop("password")

    #     response = requests.post(
    #         f"{BASE_URL}{COURIER_LOGIN_ENDPOINT}",
    #         json=payload
    #     )

    #     print(response.status_code)
    #     print(response.text)
