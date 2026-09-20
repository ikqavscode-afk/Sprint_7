import pytest
import requests

from data import (
    BASE_URL,
    COURIER_ENDPOINT,
    COURIER_LOGIN_ENDPOINT,
    COURIER_DELETE_ENDPOINT
)
from helpers import generate_courier_data


@pytest.fixture
def courier_data():
    return generate_courier_data()


@pytest.fixture
def cleanup_courier():
    courier_ids = []

    yield courier_ids

    for courier_id in courier_ids:
        requests.delete(
            f"{BASE_URL}{COURIER_DELETE_ENDPOINT.format(courier_id=courier_id)}"
        )


@pytest.fixture
def courier():
    payload = generate_courier_data()

    response = requests.post(
        f"{BASE_URL}{COURIER_ENDPOINT}",
        json=payload
    )

    assert response.status_code == 201
    assert response.json()["ok"] is True

    login_response = requests.post(
        f"{BASE_URL}{COURIER_LOGIN_ENDPOINT}",
        json=payload
    )

    assert login_response.status_code == 200

    courier_id = login_response.json()["id"]

    yield payload, courier_id

    requests.delete(
        f"{BASE_URL}{COURIER_DELETE_ENDPOINT.format(courier_id=courier_id)}"
    )
    