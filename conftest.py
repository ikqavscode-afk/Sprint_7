import pytest

from api import ScooterApi
from helpers import generate_courier_data


@pytest.fixture
def api():
    # API-клиент.
    # Все HTTP-запросы выполняются через api.py.
    return ScooterApi()


@pytest.fixture
def courier_data():
    # Тестовые данные для создания нового курьера.
    return generate_courier_data()


@pytest.fixture
def cleanup_couriers(api):
    courier_ids = []

    def add_courier(courier_id):
        # fixture запоминает ID курьера для последующего удаления.
        courier_ids.append(courier_id)

    yield add_courier

    # fixture сама отвечает за очистку созданных во время теста курьеров.
    for courier_id in courier_ids:
        api.delete_courier(courier_id)


@pytest.fixture
def courier(api):
    payload = generate_courier_data()


    api.create_courier(payload)

    login_response = api.login_courier({
        "login": payload["login"],
        "password": payload["password"]
    })

    courier_id = login_response.json()["id"]

    yield payload, courier_id

    # удаление выполняется через API-клиент.
    api.delete_courier(courier_id)