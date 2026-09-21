import allure
import pytest

from data import (
    ORDER_DATA_BLACK,
    ORDER_DATA_GREY,
    ORDER_DATA_BLACK_GREY,
    ORDER_DATA_WITHOUT_COLOR
)


@allure.feature("Заказы")
@allure.story("Создание заказа")
class TestCreateOrder:

    @allure.title("Создание заказа с разными вариантами цвета")
    @pytest.mark.parametrize(
        "payload",
        [
            ORDER_DATA_BLACK,
            ORDER_DATA_GREY,
            ORDER_DATA_BLACK_GREY,
            ORDER_DATA_WITHOUT_COLOR
        ],
        ids=[
            "BLACK",
            "GREY",
            "BLACK_AND_GREY",
            "WITHOUT_COLOR"
        ]
    )
    def test_create_order(self, api, payload):
        # каждый параметр является готовым телом запроса.
        response = api.create_order(payload)

        assert response.status_code == 201
        assert "track" in response.json()
