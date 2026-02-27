import pytest


class Payloads:
    # Admin Payload
    def officer_payload(self):
        return {
            "first_name": "BaseFirst",
            "last_name": "BaseLast",
            "is_admin": True,
            "has_kilo_access": True,
            "password": "SomePassword123$"
        }

    # NonAdmin Payload
    def non_admin_payload(self):
        return {
            "first_name": "User1First",
            "last_name": "User1Last",
            "is_admin": False,
            "has_kilo_access": False,
            "password": "AnotherPassword123$"
        }


class TestSigninAuth(Payloads):

    # Officer signin success
    def test_officer_signin_success(self, client):
        request = client.post("/test", json=self.officer_payload())
        request = client.post("/signin", json=self.officer_payload())

        assert request.status_code == 200

    # Officer signin failure
    def test_officer_signin_fail_nonadmin(self, client):
        request = client.post("/signin", json=self.non_admin_payload())

        assert request.status_code == 401

    def test_officer_signin_fail_no_password(self, client):
        request = client.post("/test", json=self.officer_payload())
        request = client.post("/signin", json={
            "first_name": "BaseFirst",
            "last_name": "BaseLast",
            "password": ""
        })

        assert request.status_code == 400

    def test_officer_signin_fail_no_first(self, client):
        request = client.post("/test", json=self.officer_payload())
        request = client.post("/signin", json={
            "first_name": "",
            "last_name": "BaseLast",
            "password": "SomePassword123$"
        })

        assert request.status_code == 400

    def test_officer_signin_fail_no_last(self, client):
        request = client.post("/test", json=self.officer_payload())
        request = client.post("/signin", json={
            "first_name": "BaseFirst",
            "last_name": "",
            "password": "SomePassword123$"
        })

        assert request.status_code == 400

    def test_officer_signin_fail_wrong_password(self, client):
        request = client.post("/test", json=self.officer_payload())
        request = client.post("/signin", json={
            "first_name": "BaseFirst",
            "last_name": "BaseLast",
            "password": "WrongPassword"
        })

        assert request.status_code == 401


class TestSignoutAuth(Payloads):
    def test_officer_signout_success(self, client, auth_token):
        request = client.post(
            "/signout", headers={'Authorization': f'Bearer {auth_token}'})

        assert request.status_code == 200

    def test_officer_signout_fail_no_jwt(self, client):
        request = client.post(
            "/signout")

        assert request.status_code == 401


class TestRefreshAuth(Payloads):
    @pytest.fixture(autouse=True)
    def refresh_tokens(self, client):
        # Create officer
        client.post("/test", json=self.officer_payload())

        # Sign in officer and get both tokens
        signin_response = client.post("/signin", json=self.officer_payload())
        data = signin_response.get_json()
        access_token = data["access_token"]

        refresh_token = data.get("refresh_token")
        return {"access": access_token, "refresh": refresh_token}

    def test_refresh_token_success(self, client, auth_token, refresh_tokens):
        refresh_token = refresh_tokens["refresh"]

        response = client.post(
            "/refresh",
            headers={'Authorization': f'Bearer {auth_token}'},
            json={"refresh_token": refresh_token}
        )

        print("Refresh response:", response.get_json())  # debug
        assert response.status_code == 200
        assert "access_token" in response.get_json()

    def test_refresh_token_missing(self, client, auth_token):
        response = client.post(
            "/refresh",
            headers={'Authorization': f'Bearer {auth_token}'},
            json={})

        assert response.status_code == 400
