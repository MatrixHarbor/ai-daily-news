import json
import requests
from geojson import Point
from urllib.parse import urlencode, quote
# API endpoint URL's and access keys
WMATA_API_KEY = "9c417af546b84d798ac197afd1a1039b" # https://developer.wmata.com/demokey
MAPBOX_API_KEY = "pk.eyJ1IjoiaGFydmV5NzUzIiwiYSI6ImNtMjd2Y2F5azFmZzAybW42eHd1eDYyYm4ifQ.m63GYztYTfxreurOr_E2rQ"
INCIDENTS_URL = "https://api.wmata.com/Incidents.svc/json/ElevatorIncidents"
STATION_URL = "https://api.wmata.com/Rail.svc/json/jStationInfo"
MAPBOX_URL = "https://api.mapbox.com/styles/v1/mapbox/streets-v12/static"
headers = {"api_key": WMATA_API_KEY, 'Accept': '*/*'}
# MapBox URL parameters
CENTER_POINT = "-77.054,38.942"
ZOOM_LEVEL = "9"
DIMENSIONS = "500x500"
MAPBOX_URL_PARAMS = f"{CENTER_POINT},{ZOOM_LEVEL}/{DIMENSIONS}"
################################################################################
# query the WMATA 'ElevatorIncidents' API to get a list of outages
def get_station_incidents():
    response = requests.get(INCIDENTS_URL,headers=headers)
    data = response.json()
    station_codes = set()
    for incident in data.get("ElevatorIncidents",[]):
        station_code = incident.get("StationCode")
        if station_code:
            station_codes.add(station_code)
    return station_codes
# use 'requests' to retrieve escalator/elevator incident information
# docs: https://developer.wmata.com/docs/services/54763641281d83086473f232/operations/54763641281d830c946a3d76?
# parse the JSON response of all incidents and create a set containing the station codes
# return the set
################################################################################
# query the WMATA 'Stations' API to get location coordinates (lat/lon)
def get_station_info(station_code: str):
    url = f"{STATION_URL}?StationCode={station_code}&api_key={WMATA_API_KEY}"
    response = requests.get(url, headers=headers)
    return response.json()
# use 'requests' to retrive station information by station code
# docs: https://developer.wmata.com/docs/services/5476364f031f590f38092507/operations/5476364f031f5909e4fe3310?
# return the response as JSON
################################################################################
# # convert list lat/lon pairs (tuples) to URL-encoded GeoJSON object
def encode_geojson(incident_locations):
    feature_collection = {"type":"FeatureCollection","features":[]}
# build out FeatureCollection to contain a list of "features"
# each "feature" contains a GeoJSON object that will be plotted as a map marker
    for location in incident_locations:
            feature = {
                "type":"Feature","properties":
                {"marker-color":"#462eff",
                 "marker-size":"small",
                 "marker-symbol":"caution"},
                "geometry": Point(location)}
            feature_collection["features"].append(feature)
    # return URL-encoded (quoted) GeoJSON object
    return quote(json.dumps(feature_collection))
################################################################################
# retrieve static map image with GeoJSON multiple marker overlay
def get_static_map(encoded_geo_json):
    static_map_url = f"{MAPBOX_URL}/geojson({encoded_geo_json})/{MAPBOX_URL_PARAMS}?access_token={MAPBOX_API_KEY}"
    response = requests.get(static_map_url)
    if response.status_code == 200:
        with open("map.png","wb") as f:
            f.write(response.content)
    else:
        print("Error returned from MapBox API")
# MapBox static map URL for 500x500 image centered at (-77.054,38.942) lon/lat
# use 'requests' and the static_map_url to retrieve the map image
# if the status code is 200, write the raw bytes (binary data) in the response to a new file called map.png
# else print "Error returned from MapBoxAPI"
################################################################################
def main():
    station_codes = get_station_incidents()
    print(f"{len(station_codes)} stations are currently experiencing accessibility outages.")
    incident_locations = []
    for station_code in list(station_codes)[:20]:
        station_info = get_station_info(station_code)
        lon = station_info.get("Lon")
        lat = station_info.get("Lat")
        if lon and lat:
            incident_locations.append((lon,lat))
            print(station_info.get("Name"))
    encoded_geo_json = encode_geojson(incident_locations)
    get_static_map(encoded_geo_json)
# get a set of unique station codes experiencing outages
# print the total number of stations with outages
# format: X stations are currently experiencing accessibility outages.
# print the name of each station with an outage
# build a list of lon/lat pairs (tuples) of the location of the first 20 stations with an outage
# format: [(lon1, lat1), (lon2, lat2), ..., ()]
# convert the list of lon/lat pairs to a URL-encoded GeoJSON blob using the provided 'encode_geojson' function
# hint: just pass the result of the previous step (the list of lon/lat tuples) to the 'encode_geojson' function
# use the provided 'get_static_map' function to retrieve and download the static map image
# hint: pass the return value from the previous step to the 'get_static_map' function
################################################################################
if __name__ == "__main__":
    main()