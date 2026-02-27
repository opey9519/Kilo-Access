import pytest


class TestAdmin:
    # Admin Payload
    def base_admin_payload(self):
        return {
            "first_name": "BaseFirst",
            "last_name": "BaseLast",
            "is_admin": True,
            "has_kilo_access": True,
            "password": "SomePassword123$"
        }

    # Tests Base Admin creation
    def test_base_admin_created(self, client):
        request = client.post("/test", json=self.base_admin_payload())

        assert request.status_code == 201
