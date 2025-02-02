import json
import requests
from flask import Flask

# API endpoint URL and access keys
WMATA_API_KEY = "9c417af546b84d798ac197afd1a1039b"  # Replace with your actual WMATA API key
INCIDENTS_URL = "https://api.wmata.com/Incidents.svc/json/ElevatorIncidents"
headers = {"api_key": WMATA_API_KEY, 'Accept': '*/*'}

# Initialize Flask app
app = Flask(__name__)

# Get incidents by machine type (elevators/escalators)
@app.route("/incidents/<unit_type>", methods=["GET"])
def get_incidents(unit_type):
    # Step 1: Create an empty list called 'incidents'
    incidents = []

    # Step 2: Use 'requests' to make a GET request to the WMATA Incidents API
    response = requests.get(INCIDENTS_URL, headers=headers)

    # Step 3: Retrieve the JSON data from the response
    data = response.json()

    # Check if there are incidents in the response
    if not data.get("ElevatorIncidents"):
        return json.dumps([])  # Return an empty JSON list if no incidents are found

    # Step 4: Iterate through the JSON response and retrieve all incidents matching 'unit_type'
    for incident in data.get("ElevatorIncidents", []):
        # Check if the incident's unit type matches the requested unit_type
        if incident.get("UnitType").lower() == unit_type.lower():
            # Step 5: Create a dictionary containing the 4 fields from Module 7
            incident_info = {
                "StationCode": incident.get("StationCode"),
                "StationName": incident.get("StationName"),
                "UnitName": incident.get("UnitName"),
                "UnitType": incident.get("UnitType")
            }
            # Step 6: Add each incident dictionary object to the 'incidents' list
            incidents.append(incident_info)

    # Step 7: Return the list of incident dictionaries as a JSON string using json.dumps
    return json.dumps(incidents)

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)

