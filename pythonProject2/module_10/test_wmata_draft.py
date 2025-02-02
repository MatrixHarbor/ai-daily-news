from wmata_api_draft import app
import json
import unittest


class WMATATest(unittest.TestCase):

    # Ensure both endpoints return a 200 HTTP code
    def test_http_success(self):
        # Test /incidents/escalators
        escalator_response = app.test_client().get('/incidents/escalators').status_code
        self.assertEqual(escalator_response, 200, "Expected 200 HTTP status for escalators endpoint")

        # Test /incidents/elevators
        elevator_response = app.test_client().get('/incidents/elevators').status_code
        self.assertEqual(elevator_response, 200, "Expected 200 HTTP status for elevators endpoint")

    ################################################################################
    # Ensure all returned incidents have the 4 required fields
    def test_required_fields(self):
        required_fields = ["StationCode", "StationName", "UnitType", "UnitName"]

        # Get response from /incidents/escalators
        response = app.test_client().get('/incidents/escalators')
        json_response = json.loads(response.data.decode())

        # Skip the test if no incidents are returned
        if not json_response:
            self.skipTest("No incidents returned from /incidents/escalators endpoint")

        # Check each incident for required fields
        for incident in json_response:
            for field in required_fields:
                self.assertIn(field, incident, f"Expected field '{field}' in the incident data")

    ################################################################################
    # Ensure all entries returned by the /escalators endpoint have a UnitType of "ESCALATOR"
    def test_escalators(self):
        response = app.test_client().get('/incidents/escalators')
        json_response = json.loads(response.data.decode())

        # Skip the test if no incidents are returned
        if not json_response:
            self.skipTest("No incidents returned from /incidents/escalators endpoint")

        # Check that each incident has 'UnitType' equal to "ESCALATOR"
        for incident in json_response:
            self.assertEqual(incident["UnitType"].upper(), "ESCALATOR", "Expected UnitType to be 'ESCALATOR'")

    ################################################################################
    # Ensure all entries returned by the /elevators endpoint have a UnitType of "ELEVATOR"
    def test_elevators(self):
        response = app.test_client().get('/incidents/elevators')
        json_response = json.loads(response.data.decode())

        # Skip the test if no incidents are returned
        if not json_response:
            self.skipTest("No incidents returned from /incidents/elevators endpoint")

        # Check that each incident has 'UnitType' equal to "ELEVATOR"
        for incident in json_response:
            self.assertEqual(incident["UnitType"].upper(), "ELEVATOR", "Expected UnitType to be 'ELEVATOR'")


################################################################################
if __name__ == "__main__":
    unittest.main()