import allure
import requests

from data import (
    BASE_URL,
    COURIER_ENDPOINT,
    COURIER_LOGIN_ENDPOINT,
    COURIER_DELETE_ENDPOINT,
    ORDER_ENDPOINT
)


class ScooterApi:

    @allure.step("Создать курьера")
    def create_courier(self, payload):
        # HTTP-запрос вынесен из теста в отдельный API-метод.
        return requests.post(
            f"{BASE_URL}{COURIER_ENDPOINT}",
            json=payload
        )

    @allure.step("Авторизовать курьера")
    def login_courier(self, payload):
        # Запрос авторизации теперь выполняется через API-клиент.
        return requests.post(
            f"{BASE_URL}{COURIER_LOGIN_ENDPOINT}",
            json=payload
        )

    @allure.step("Удалить курьера")
    def delete_courier(self, courier_id):
        # Удаление курьера также вынесено из fixture.
        return requests.delete(
            f"{BASE_URL}{COURIER_DELETE_ENDPOINT.format(courier_id=courier_id)}"
        )

    @allure.step("Создать заказ")
    def create_order(self, payload):
        # Запрос создания заказа вынесен в API-клиент.
        return requests.post(
            f"{BASE_URL}{ORDER_ENDPOINT}",
            json=payload
        )

    @allure.step("Получить список заказов")
    def get_orders(self):
        # GET-запрос вынесен в API-клиент.
        return requests.get(
            f"{BASE_URL}{ORDER_ENDPOINT}"
        )
    