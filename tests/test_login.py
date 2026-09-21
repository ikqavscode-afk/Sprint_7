import allure


@allure.feature("Курьер")
@allure.story("Авторизация курьера")
class TestCourierLogin:

    @allure.title("Успешная авторизация курьера")
    def test_login_success(self, api, courier):
        payload, courier_id = courier

        # запрос через API-клиент..
        response = api.login_courier(payload)

        assert response.status_code == 200
        assert "id" in response.json()
        assert response.json()["id"] == courier_id

    @allure.title("Авторизация с неверным паролем")
    def test_login_wrong_password(self, api, courier):
        payload, _ = courier

        payload["password"] = "wrong_password"

        # запрос через API-клиент.
        response = api.login_courier(payload)

        assert response.status_code == 404
        assert response.json()["message"] == "Учетная запись не найдена"

    @allure.title("Авторизация с неверным логином")
    def test_login_wrong_login(self, api, courier):
        payload, _ = courier

        payload["login"] = "wrong_login"

        # запрос через API-клиент.
        response = api.login_courier(payload)

        assert response.status_code == 404
        assert response.json()["message"] == "Учетная запись не найдена"

    @allure.title("Авторизация без логина")
    def test_login_without_login(self, api, courier):
        payload, _ = courier

        payload.pop("login")

        # запрос через API-клиент.
        response = api.login_courier(payload)

        assert response.status_code == 400
        assert response.json()["message"] == "Недостаточно данных для входа"
