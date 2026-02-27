import pytest
from server.app import create_app, db


@pytest.fixture
def app():
    app = create_app("testing")

    with app.app_context():
        db.create_all()
        yield app
        db.session.remove()
        db.drop_all()


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture()
def auth_token(client):
    officer_payload = {
        "first_name": "BaseFirst",
        "last_name": "BaseLast",
        "is_admin": True,
        "has_kilo_access": True,
        "password": "SomePassword123$"
    }

    # Create officer
    client.post("/test", json=officer_payload)

    # Sign in officer
    signin_response = client.post("/signin", json=officer_payload)
    token = signin_response.get_json()["access_token"]

    return token
