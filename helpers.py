import uuid

def generate_courier_data():
    unique_login = f"test_{uuid.uuid4().hex[:8]}"

    return {
        "login": unique_login,
        "password": "password123",
        "firstName": "Test"
    }