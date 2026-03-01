class Payloads():
    # Officer Payload - Used to create secondhand Officers
    def officer_payload(self):
        return {
            "first_name": "OfficerFirst",
            "last_name": "OfficerLast",
            "is_admin": True,
            "kilo_access": True,
            "password": "AnotherOfficerPassword123$"
        }

    # Athlete Payload - Used to create Athletes
    def athlete_payload(self):
        return {
            "first_name": "AthleteFirst",
            "last_name": "AthleteLast",
            "is_admin": False,
            "kilo_access": False
        }


class TestGet(Payloads):
    def test_get_all_success(self, client):
        get_all_response = client.get("/users")
        assert get_all_response.status_code == 200

        users = get_all_response.get_json()["users"]

        assert isinstance(users, list)

    def test_get_athlete_success(self, client, auth_token):
        client.post(
            "/athlete",
            headers={'Authorization': f'Bearer {auth_token}',
                     "Content-Type": "application/json"},
            json=self.athlete_payload()
        )
        get_athlete_response = client.get("/athlete/1")
        assert get_athlete_response.status_code == 200

        user = get_athlete_response.get_json()
        assert isinstance(user, dict)

    def test_get_athlete_fail_not_found(self, client):
        get_athlete_response = client.get("/athlete/1")
        assert get_athlete_response.status_code == 404

    def test_get_officer_success(self, client, auth_token):
        client.post(
            "/officer",
            headers={'Authorization': f'Bearer {auth_token}',
                     "Content-Type": "application/json"},
            json=self.officer_payload()
        )
        get_officer_response = client.get("/officer/1")
        assert get_officer_response.status_code == 200

        officer = get_officer_response.get_json()
        assert isinstance(officer, dict)

    def test_get_officer_fail_not_found(self, client):
        get_officer_response = client.get("/officer/1")
        assert get_officer_response.status_code == 404
