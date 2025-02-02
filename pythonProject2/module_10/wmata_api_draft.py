import json
import requests
from flask import Flask, jsonify

# API endpoint URL and access keys
WMATA_API_KEY = "9c417af546b84d798ac197afd1a1039b"
INCIDENTS_URL = "https://api.wmata.com/Incidents.svc/json/ElevatorIncidents"
headers = {"api_key": WMATA_API_KEY, 'Accept': '*/*'}

# Initialize Flask app
app = Flask(__name__)

# Get incidents by machine type (elevators/escalators)
@app.route("/incidents/<unit_type>", methods=["GET"])

def get_incidents(unit_type):
    # Step 1: Create an empty list called 'incidents'
    incidents = []

    # Step 2: Use 'requests' to do a GET request to the WMATA Incidents API
    response = requests.get(INCIDENTS_URL, headers=headers)

    # Step 3: Check if the response was successful
    if response.status_code != 200:
        return Response(json.dumps({"error": "Failed to retrieve data from WMATA API"}), status=500, mimetype='application/json')

    # Step 4: Retrieve the JSON from the response and inspect the data structure
    data = response.json()
    print(data)  # Temporary print statement to check the returned data

    # Step 5: Iterate through the JSON response and retrieve all incidents matching 'unit_type'
    for incident in data.get("ElevatorIncidents", []):
        # Only add incidents that match the unit_type (e.g., "elevators" or "escalators")
        if incident.get("UnitType", "").lower() == unit_type.lower():
            # Create a dictionary with the required fields
            incident_info = {
                "StationCode": incident.get("StationCode"),
                "StationName": incident.get("StationName"),
                "UnitName": incident.get("UnitName"),
                "UnitType": incident.get("UnitType")
            }
            # Add the incident dictionary to the 'incidents' list
            incidents.append(incident_info)

    # Step 6: Return the list of incident dictionaries as a JSON string using json.dumps()
    return Response(json.dumps(incidents), mimetype='application/json')

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)