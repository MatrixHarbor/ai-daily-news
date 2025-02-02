import json
import requests
from geojson import Point
from urllib.parse import quote

# API endpoint URLs and access keys
WMATA_API_KEY = "3124748f5021427f83f566448026f084"
MAPBOX_API_KEY = "pk.eyJ1Ijoic2hlbGxleTgyMSIsImEiOiJjbTI4Nng3NzUxMm40MnBxMGliaWprYnIyIn0.O8x9z_xlZd3DqS13LYr9Xw"
INCIDENTS_URL = "https://api.wmata.com/Incidents.svc/json/ElevatorIncidents"
STATION_URL = "https://api.wmata.com/Rail.svc/json/jStationInfo"
MAPBOX_URL = "https://api.mapbox.com/styles/v1/mapbox/streets-v12/static"
headers = {"api_key": WMATA_API_KEY, 'Accept': '*/*'}

# MapBox URL parameters
CENTER_POINT = "-77.054,38.942"
ZOOM_LEVEL = "9"
DIMENSIONS = "500x500"
MAPBOX_URL_PARAMS = f"{CENTER_POINT},{ZOOM_LEVEL}/{DIMENSIONS}"


# Query the WMATA 'ElevatorIncidents' API to get a list of outages
def get_station_incidents():
    response = requests.get(INCIDENTS_URL, headers=headers)
    if response.status_code == 200:
        incidents = response.json()
        elevator_incidents = incidents.get('ElevatorIncidents', [])
        # Ensure 'StationCode' exists in each incident
        station_codes = set([incident['StationCode'] for incident in elevator_incidents if 'StationCode' in incident])
        return station_codes
    else:
        print(f"Failed to retrieve incidents: {response.status_code}")
        return set()


# Query the WMATA 'Stations' API to get location coordinates (lat/lon)
def get_station_info(station_code: str):
    params = {"StationCode": station_code}
    response = requests.get(STATION_URL, headers=headers, params=params)
    if response.status_code == 200:
        station_info = response.json()
        station_name = station_info.get("Name")
        latitude = station_info.get("Lat")
        longitude = station_info.get("Lon")
        if latitude and longitude:  # Ensure both lat and lon exist
            # Print station info in the same format as your version
            print(station_name)
            return (longitude, latitude)  # Returning coordinates in (lon, lat) format
    else:
        print(f"Failed to retrieve data for station code: {station_code}")
    return None


# Convert list of lon/lat pairs (tuples) to URL-encoded GeoJSON object
def encode_geojson(incident_locations):
    feature_collection = {"type": "FeatureCollection", "features": []}
    for location in incident_locations:
        feature = {"type": "Feature", "properties":
            {"marker-color": "#462eff", "marker-size": "small", "marker-symbol": "caution"},
                   "geometry": Point(location)}
        feature_collection["features"].append(feature)
    return quote(json.dumps(feature_collection))


# Retrieve static map image with GeoJSON multiple marker overlay
def get_static_map(encoded_geo_json):
    static_map_url = f"{MAPBOX_URL}/geojson({encoded_geo_json})/{MAPBOX_URL_PARAMS}?access_token={MAPBOX_API_KEY}"

    # Debugging: Print the generated URL to check if it's correct

    response = requests.get(static_map_url)

    if response.status_code == 200:
        with open("map.png", "wb") as map_file:
            map_file.write(response.content)
    else:
        print(f"Error returned from MapBox API: {response.status_code}")
        print(f"Response Text: {response.text}")


def main():
    # Get a set of unique station codes experiencing outages
    station_codes = get_station_incidents()
    # Ensure station codes are unique and print the total count
    unique_station_codes = list(station_codes)  # Ensure station codes are unique
    print(f"{len(unique_station_codes)} stations are currently experiencing accessibility outages.")

    incident_locations = []
    for code in unique_station_codes[:20]:
        location = get_station_info(code)
        if location:
            incident_locations.append(location)
    encoded_geo_json = encode_geojson(incident_locations)
    get_static_map(encoded_geo_json)


if __name__ == "__main__":
    main()