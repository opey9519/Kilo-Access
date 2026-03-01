# test_admin.py contains tests correlating to ../server/app/api/admin.py

'''
    Payloads Class used to abstract POST, PATCH, PUT http methods
'''


class Payloads:
    # Admin Payload - Used to create first account
    def base_admin_payload(self):
        return {
            "first_name": "BaseFirst",
            "last_name": "BaseLast",
            "is_admin": True,
            "kilo_access": True,
            "password": "SomePassword123$"
        }

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


####################################################################################
'''
    Test POST methods on athlete and officers
    Uses json payloads from the Payloads class
    Uses in-line payload adjustments for specific test cases
'''


class TestCreate(Payloads):
    # Tests Base Admin creation
    def test_base_admin_created(self, client):
        request = client.post("/test", json=self.base_admin_payload())

        assert request.status_code == 201

    # Test creation
    def test_create_athlete_success(self, client, auth_token):
        create_athlete_response = client.post(
            "/athlete",
            headers={'Authorization': f'Bearer {auth_token}',
                     "Content-Type": "application/json"},
            json=self.athlete_payload(),
        )

        assert create_athlete_response.status_code == 201

    def test_create_athlete_fail_no_jwt(self, client):
        create_athlete_response = client.post(
            "/athlete",
            json=self.athlete_payload()
        )

        assert create_athlete_response.status_code == 401

    def test_create_athlete_fail_already_exists(self, client, auth_token):
        client.post(
            "athlete",
            headers={'Authorization': f'Bearer {auth_token}',
                     "Content-Type": "application/json"},
            json=self.athlete_payload()
        )

        create_athlete_response = client.post(
            "athlete",
            headers={'Authorization': f'Bearer {auth_token}',
                     "Content-Type": "application/json"},
            json=self.athlete_payload()
        )

        assert create_athlete_response.status_code == 409

    def test_create_athlete_fail_no_first_name(self, client, auth_token):
        create_athlete_response = client.post(
            "athlete",
            headers={'Authorization': f'Bearer {auth_token}',
                     "Content-Type": "application/json"},
            json={
                "first_name": "",
                "last_name": "AthleteLast",
                "is_admin": False,
                "kilo_access": False
            }
        )

        assert create_athlete_response.status_code == 400

    def test_create_athlete_fail_no_last_name(self, client, auth_token):
        create_athlete_response = client.post(
            "athlete",
            headers={'Authorization': f'Bearer {auth_token}',
                     "Content-Type": "application/json"},
            json={
                "first_name": "AthleteFirst",
                "last_name": "",
                "is_admin": False,
                "kilo_access": False
            }
        )

        assert create_athlete_response.status_code == 400

    def test_create_officer_success(self, client, auth_token):
        create_officer_response = client.post(
            "/officer",
            headers={'Authorization': f'Bearer {auth_token}',
                     "Content-Type": "application/json"},
            json=self.officer_payload()
        )

        assert create_officer_response.status_code == 201

    def test_create_officer_fail_no_jwt(self, client):
        create_officer_response = client.post(
            "/officer",
            json=self.officer_payload()
        )

        assert create_officer_response.status_code == 401

    def test_create_officer_fail_already_exists(self, client, auth_token):
        client.post(
            "/officer",
            headers={'Authorization': f'Bearer {auth_token}',
                     "Content-Type": "application/json"},
            json=self.officer_payload()
        )

        create_officer_response = client.post(
            "/officer",
            headers={'Authorization': f'Bearer {auth_token}',
                     "Content-Type": "application/json"},
            json=self.officer_payload()
        )

        assert create_officer_response.status_code == 409

    def test_create_officer_fail_no_first_name(self, client, auth_token):
        create_officer_response = client.post(
            "/officer",
            headers={'Authorization': f'Bearer {auth_token}',
                     "Content-Type": "application/json"},
            json={
                "first_name": "",
                "last_name": "OfficerLast",
                "is_admin": True,
                "kilo_access": True,
                "password": "AnotherOfficerPassword123$"
            }
        )

        assert create_officer_response.status_code == 400

    def test_create_officer_fail_no_last_name(self, client, auth_token):
        create_officer_response = client.post(
            "/officer",
            headers={'Authorization': f'Bearer {auth_token}',
                     "Content-Type": "application/json"},
            json={
                "first_name": "OfficerFirst",
                "last_name": "",
                "is_admin": True,
                "kilo_access": True,
                "password": "AnotherOfficerPassword123$"
            }
        )

        assert create_officer_response.status_code == 400

    def test_create_officer_fail_no_password(self, client, auth_token):
        create_officer_response = client.post(
            "/officer",
            headers={'Authorization': f'Bearer {auth_token}',
                     "Content-Type": "application/json"},
            json={
                "first_name": "OfficerFirst",
                "last_name": "OfficerLast",
                "is_admin": True,
                "kilo_access": True,
                "password": ""
            }
        )

        assert create_officer_response.status_code == 400


####################################################################################
'''
    Test PUT methods on athlete and officers
    Uses json payloads from the Payloads class
    Uses in-line payload adjustments for specific test cases
'''


class TestEdit(Payloads):
    def test_edit_athlete_success(self, client, auth_token):
        client.post(
            "/athlete",
            headers={'Authorization': f'Bearer {auth_token}',
                     "Content-Type": "application/json"},
            json=self.athlete_payload(),
        )

        edit_athlete_response = client.put(
            "/athlete/1",
            headers={'Authorization': f'Bearer {auth_token}',
                     "Content-Type": "application/json"},
            json={
                "new_first_name": "NewAthleteFirst",
                "new_last_name": "NewAthleteLast",
                "kilo_access": True
            }
        )

        assert edit_athlete_response.status_code == 200

    def test_edit_athlete_fail_no_jwt(self, client, auth_token):
        client.post(
            "/athlete",
            headers={'Authorization': f'Bearer {auth_token}',
                     "Content-Type": "application/json"},
            json=self.athlete_payload(),
        )

        edit_athlete_response = client.put(
            "/athlete/999",
            json={
                "new_first_name": "NewAthleteFirst",
                "new_last_name": "NewAthleteLast",
                "kilo_access": True
            }
        )

        assert edit_athlete_response.status_code == 401

    def test_edit_athlete_fail_not_found(self, client, auth_token):
        client.post(
            "/athlete",
            headers={'Authorization': f'Bearer {auth_token}',
                     "Content-Type": "application/json"},
            json=self.athlete_payload(),
        )

        edit_athlete_response = client.put(
            "/athlete/999",
            headers={'Authorization': f'Bearer {auth_token}',
                     "Content-Type": "application/json"},
            json={
                "new_first_name": "NewAthleteFirst",
                "new_last_name": "NewAthleteLast",
                "kilo_access": True
            }
        )

        assert edit_athlete_response.status_code == 404

    def test_edit_athlete_fail_no_first_name(self, client, auth_token):
        client.post(
            "/athlete",
            headers={'Authorization': f'Bearer {auth_token}',
                     "Content-Type": "application/json"},
            json=self.athlete_payload(),
        )

        edit_athlete_response = client.put(
            "/athlete/1",
            headers={'Authorization': f'Bearer {auth_token}',
                     "Content-Type": "application/json"},
            json={
                "new_first_name": "",
                "new_last_name": "NewAthleteLast",
                "kilo_access": True
            }
        )

        assert edit_athlete_response.status_code == 400

    def test_edit_athlete_fail_no_last_name(self, client, auth_token):
        client.post(
            "/athlete",
            headers={'Authorization': f'Bearer {auth_token}',
                     "Content-Type": "application/json"},
            json=self.athlete_payload(),
        )

        edit_athlete_response = client.put(
            "/athlete/1",
            headers={'Authorization': f'Bearer {auth_token}',
                     "Content-Type": "application/json"},
            json={
                "new_first_name": "NewAthleteFirst",
                "new_last_name": "",
                "kilo_access": True
            }
        )

        assert edit_athlete_response.status_code == 400

    def test_edit_officer_success(self, client, auth_token):
        client.post(
            "/officer",
            headers={'Authorization': f'Bearer {auth_token}',
                     "Content-Type": "application/json"},
            json=self.officer_payload(),
        )

        edit_officer_response = client.put(
            "/officer/1",
            headers={'Authorization': f'Bearer {auth_token}',
                     "Content-Type": "application/json"},
            json={
                "new_first_name": "NewOfficerFirst",
                "new_last_name": "NewOfficerLast",
                "kilo_access": True
            }
        )

        assert edit_officer_response.status_code == 200

    def test_edit_officer_fail_no_jwt(self, client, auth_token):
        client.post(
            "/officer",
            headers={'Authorization': f'Bearer {auth_token}',
                     "Content-Type": "application/json"},
            json=self.officer_payload(),
        )

        edit_officer_response = client.put(
            "/officer/1",
            json={
                "new_first_name": "NewOfficerFirst",
                "new_last_name": "NewOfficerLast",
                "kilo_access": True
            }
        )

        assert edit_officer_response.status_code == 401

    def test_edit_officer_fail_not_found(self, client, auth_token):
        client.post(
            "/officer",
            headers={'Authorization': f'Bearer {auth_token}',
                     "Content-Type": "application/json"},
            json=self.officer_payload(),
        )

        edit_officer_response = client.put(
            "/officer/999",
            headers={'Authorization': f'Bearer {auth_token}',
                     "Content-Type": "application/json"},
            json={
                "new_first_name": "NewOfficerFirst",
                "new_last_name": "NewOfficerLast",
                "kilo_access": True
            }
        )

        assert edit_officer_response.status_code == 404

    def test_edit_officer_fail_no_first_name(self, client, auth_token):
        client.post(
            "/officer",
            headers={'Authorization': f'Bearer {auth_token}',
                     "Content-Type": "application/json"},
            json=self.officer_payload(),
        )

        edit_officer_response = client.put(
            "/officer/1",
            headers={'Authorization': f'Bearer {auth_token}',
                     "Content-Type": "application/json"},
            json={
                "new_first_name": "",
                "new_last_name": "NewOfficerLast",
                "kilo_access": True
            }
        )

        assert edit_officer_response.status_code == 400

    def test_edit_officer_fail_no_last_name(self, client, auth_token):
        client.post(
            "/officer",
            headers={'Authorization': f'Bearer {auth_token}',
                     "Content-Type": "application/json"},
            json=self.officer_payload(),
        )

        edit_officer_response = client.put(
            "/officer/1",
            headers={'Authorization': f'Bearer {auth_token}',
                     "Content-Type": "application/json"},
            json={
                "new_first_name": "NewOfficerFirst",
                "new_last_name": "",
                "kilo_access": True
            }
        )

        assert edit_officer_response.status_code == 400


####################################################################################
'''
    Test PATCH methods on athlete and officers
    Uses json payloads from the Payloads class
    Uses in-line payload adjustments for specific test cases
'''


class TestPatch(Payloads):
    def test_patch_athlete_success(self, client, auth_token):
        client.post(
            "/athlete",
            headers={'Authorization': f'Bearer {auth_token}',
                     "Content-Type": "application/json"},
            json=self.athlete_payload(),
        )

        patch_athlete_response = client.patch(
            "/athlete/1",
            headers={'Authorization': f'Bearer {auth_token}',
                     "Content-Type": "application/json"},
            json={"kilo_access": True}
        )

        assert patch_athlete_response.status_code == 200

    def test_patch_athlete_fail_no_jwt(self, client, auth_token):
        client.post(
            "/athlete",
            headers={'Authorization': f'Bearer {auth_token}',
                     "Content-Type": "application/json"},
            json=self.athlete_payload(),
        )

        patch_athlete_response = client.patch(
            "/athlete/1",
            json={"kilo_access": True}
        )

        assert patch_athlete_response.status_code == 401

    def test_patch_athlete_fail_not_found(self, client, auth_token):
        client.post(
            "/athlete",
            headers={'Authorization': f'Bearer {auth_token}',
                     "Content-Type": "application/json"},
            json=self.athlete_payload(),
        )

        patch_athlete_response = client.patch(
            "/athlete/999",
            headers={'Authorization': f'Bearer {auth_token}',
                     "Content-Type": "application/json"},
            json={"kilo_access": True}
        )

        assert patch_athlete_response.status_code == 404

    def test_patch_athlete_no_kilo_access(self, client, auth_token):
        client.post(
            "/athlete",
            headers={'Authorization': f'Bearer {auth_token}',
                     "Content-Type": "application/json"},
            json=self.athlete_payload(),
        )

        patch_athlete_response = client.patch(
            "/athlete/1",
            headers={'Authorization': f'Bearer {auth_token}',
                     "Content-Type": "application/json"},
            json={"kilo_access": None}
        )

        assert patch_athlete_response.status_code == 400

    def test_patch_officer_success(self, client, auth_token):
        client.post(
            "/officer",
            headers={'Authorization': f'Bearer {auth_token}',
                     "Content-Type": "application/json"},
            json=self.athlete_payload(),
        )

        patch_offier_response = client.patch(
            "/officer/1",
            headers={'Authorization': f'Bearer {auth_token}',
                     "Content-Type": "application/json"},
            json={"kilo_access": True}
        )

        assert patch_offier_response.status_code == 200

    def test_patch_officer_fail_no_jwt(self, client, auth_token):
        client.post(
            "/officer",
            headers={'Authorization': f'Bearer {auth_token}',
                     "Content-Type": "application/json"},
            json=self.athlete_payload(),
        )

        patch_offier_response = client.patch(
            "/officer/1",
            json={"kilo_access": True}
        )

        assert patch_offier_response.status_code == 401

    def test_patch_officer_fail_not_found(self, client, auth_token):
        client.post(
            "/officer",
            headers={'Authorization': f'Bearer {auth_token}',
                     "Content-Type": "application/json"},
            json=self.athlete_payload(),
        )

        patch_offier_response = client.patch(
            "/officer/999",
            headers={'Authorization': f'Bearer {auth_token}',
                     "Content-Type": "application/json"},
            json={"kilo_access": True}
        )

        assert patch_offier_response.status_code == 404

    def test_patch_officer_no_kilo_access(self, client, auth_token):
        client.post(
            "/officer",
            headers={'Authorization': f'Bearer {auth_token}',
                     "Content-Type": "application/json"},
            json=self.athlete_payload(),
        )

        patch_offier_response = client.patch(
            "/officer/1",
            headers={'Authorization': f'Bearer {auth_token}',
                     "Content-Type": "application/json"},
            json={"kilo_access": None}
        )

        assert patch_offier_response.status_code == 400


####################################################################################
'''
    Test DELETE methods on athlete and officers
    Uses json payloads from the Payloads class
    Uses in-line payload adjustments for specific test cases
'''


class TestDelete(Payloads):
    def test_delete_athlete_success(self, client, auth_token):
        client.post(
            "/athlete",
            headers={'Authorization': f'Bearer {auth_token}',
                     "Content-Type": "application/json"},
            json=self.officer_payload(),
        )

        delete_athlete_response = client.delete(
            "/athlete/1",
            headers={'Authorization': f'Bearer {auth_token}'}
        )

        assert delete_athlete_response.status_code == 200

    def test_delete_athlete_fail_no_jwt(self, client, auth_token):
        client.post(
            "/athlete",
            headers={'Authorization': f'Bearer {auth_token}',
                     "Content-Type": "application/json"},
            json=self.officer_payload(),
        )

        delete_athlete_response = client.delete(
            "/athlete/1",
        )

        assert delete_athlete_response.status_code == 401

    def test_delete_athlete_fail_not_found(self, client, auth_token):
        client.post(
            "/athlete",
            headers={'Authorization': f'Bearer {auth_token}',
                     "Content-Type": "application/json"},
            json=self.officer_payload(),
        )

        delete_athlete_response = client.delete(
            "/athlete/999",
            headers={'Authorization': f'Bearer {auth_token}'}
        )

        assert delete_athlete_response.status_code == 404

    def test_delete_officer_success(self, client, auth_token):
        client.post(
            "/officer",
            headers={'Authorization': f'Bearer {auth_token}',
                     "Content-Type": "application/json"},
            json=self.officer_payload(),
        )

        delete_officer_response = client.delete(
            "/officer/1",
            headers={'Authorization': f'Bearer {auth_token}'}
        )

        assert delete_officer_response.status_code == 200

    def test_delete_officer_fail_no_jwt(self, client, auth_token):
        client.post(
            "/officer",
            headers={'Authorization': f'Bearer {auth_token}',
                     "Content-Type": "application/json"},
            json=self.officer_payload(),
        )

        delete_officer_response = client.delete(
            "/officer/1",
        )

        assert delete_officer_response.status_code == 401

    def test_delete_officer_fail_not_found(self, client, auth_token):
        client.post(
            "/officer",
            headers={'Authorization': f'Bearer {auth_token}',
                     "Content-Type": "application/json"},
            json=self.officer_payload(),
        )

        delete_officer_response = client.delete(
            "/999",
        )

        assert delete_officer_response.status_code == 404
