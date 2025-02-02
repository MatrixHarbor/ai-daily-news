# def reverse(s):
#     if len(s) <= 1:
#         return s
#     return reverse(s[1:]) + s[0]
# print(reverse("string"))

# def encrypt(plaintext):
#     char_map = {
#         "a": "f", "b": "g", "c": "h", "d": "i", "e": "j",
#         "f": "k", "g": "l", "h": "m", "i": "n", "j": "o",
#         "k": "p", "l": "q", "m": "r", "n": "s", "o": "t",
#         "p": "u", "q": "v", "r": "w", "s": "x", "t": "y",
#         "u": "z", "v": "a", "w": "b", "x": "c", "y": "d",
#         "z": "e"
#     }
#     ciphertext = ""
#     for char in plaintext.lower():
#         if char in char_map:
#             ciphertext += char_map[char]
#         else:
#             ciphertext += char
#     return ciphertext
# s = "ATTACKATDAWN"
# print(encrypt(s))


# def bubble(lst):
#     n = len(lst)
#     for i in range(n):
#         swapped = False
#         for j in range(0, n - i - 1):
#             if lst[j] > lst[j + 1]:
#                 lst[j], lst[j + 1] = lst[j + 1], lst[j]
#                 swapped = True
#         if not swapped:
#             break
#     return lst
# unsorted_list = [3, 1, 2, 5, 6, 4]
# sorted_list = bubble(unsorted_list)
# print(sorted_list)


# year = int(input("Enter a year: "))
# if (year % 4 == 0) and ((year % 100 != 0) or (year % 400 == 0)):
#     print("Leap year!")
# else:
#     print("Not a leap year.")



# '''
# Obtain weather forecast using National Weather Service's API for a given lat/lon
#
# Example of returned json 'loc_data'
# https://api.weather.gov/points/38.8894,-77.0352
#
# Example of returned json 'weather_data'
# https://api.weather.gov/gridpoints/LWX/97,71/forecast
# '''
#
# import requests
#
# # Grab weather data for a specific latitude/longitude
# def get_weather(lat, lon):
#     base_url = f"https://api.weather.gov/points/{lat},{lon}"
#
#     ## Change below to put student Name and student email, NO ACCOUNT NEEDED ##
#     headers = {'User-Agent': 'StudentName (student_email@jhu.edu)'}
#
#     response = requests.get(base_url, headers=headers)
#     if response.status_code == 200:
#         loc_data = response.json()  # Contains location data
#         forecast_url = loc_data['properties']['forecast']  # Weather data URL
#         weather_data = requests.get(forecast_url).json()  # Contains weather data
#         return loc_data, weather_data
#
# # Main code
# def main(latitude, longitude):
#     loc_data, weather_data = get_weather(latitude, longitude)
#     city = loc_data['properties']['relativeLocation']['properties']['city']
#     today_forecast = weather_data['properties']['periods'][0]['detailedForecast']
#     print(f"The forecast for {city}:")
#     print(today_forecast)
#
# if __name__ == "__main__":
#     latitude = 39.2906
#     longitude = -76.6093
#     main(latitude, longitude)


# teams = ["Phillies", "Eagles", "76ers"]
# teams[0] = ["Flyers", "Phantoms"]
# teams += list(teams)
# teams.append("Union")

