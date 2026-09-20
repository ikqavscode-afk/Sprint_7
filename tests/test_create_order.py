import allure
import pytest
import requests

from data import BASE_URL, ORDER_ENDPOINT, ORDER_DATA


@allure.feature("Заказы")
@allure.story("Создание заказа")
class TestCreateOrder:

    @allure.title("Создание заказа с разными вариантами цвета")
    @pytest.mark.parametrize(
        "color",
        [
            ["BLACK"],
            ["GREY"],
            ["BLACK", "GREY"],
            None
        ]
    )
    def test_create_order(self, color):
        payload = ORDER_DATA.copy()

        if color is not None:
            payload["color"] = color

        response = requests.post(
            f"{BASE_URL}{ORDER_ENDPOINT}",
            json=payload
        )

        assert response.status_code == 201
        assert "track" in response.json()
        