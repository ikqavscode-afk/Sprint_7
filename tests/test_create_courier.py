import allure


@allure.feature("Курьер")
@allure.story("Создание курьера")
class TestCreateCourier:

    @allure.title("Создание нового курьера")
    def test_create_courier(self, api, courier_data, cleanup_couriers):
        # запрос создания через API-клиент.
        response = api.create_courier(courier_data)

        # ID созданного курьера для последующей очистки тестовых данных.
        login_response = api.login_courier({
            "login": courier_data["login"],
            "password": courier_data["password"]
        })

        cleanup_couriers(login_response.json()["id"])

        # тест заканчивается проверками результата.
        assert response.status_code == 201
        assert response.json()["ok"] is True

    @allure.title("Нельзя создать курьера с уже существующим логином")
    def test_create_duplicate_courier(
        self,
        api,
        courier_data,
        cleanup_couriers
    ):
        # первый запрос через API-клиент.
        response = api.create_courier(courier_data)

        # ID первого курьера для очистки.
        login_response = api.login_courier({
            "login": courier_data["login"],
            "password": courier_data["password"]
        })

        cleanup_couriers(login_response.json()["id"])

        # создать повторно курьера с тем же логином.
        duplicate_response = api.create_courier(courier_data)

        assert duplicate_response.status_code == 409
        assert duplicate_response.json()["message"] == (
            "Этот логин уже используется. Попробуйте другой."
        )

    @allure.title("Нельзя создать курьера без логина")
    def test_create_courier_without_login(self, api):
        payload = {
            "password": "password123",
            "firstName": "Test"
        }

        # запрос через API-клиент.
        response = api.create_courier(payload)

        assert response.status_code == 400
        assert response.json()["message"] == (
            "Недостаточно данных для создания учетной записи"
        )

    @allure.title("Нельзя создать курьера без пароля")
    def test_create_courier_without_password(self, api):
        payload = {
            "login": "test_without_password",
            "firstName": "Test"
        }

        # запрос через API-клиент.
        response = api.create_courier(payload)

        assert response.status_code == 400
        assert response.json()["message"] == (
            "Недостаточно данных для создания учетной записи"
        )
