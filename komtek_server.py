import requests
from pprint import pprint

places = {
    "Trondheim": {"lat": 63.43, "lon": 10.39},
    "Oslo": {"lat": 59.91, "lon": 10.75},
    "Bergen": {"lat": 60.39, "lon": 5.32},
    "Avaldsnes": {"lat": 59.35, "lon": 5.27},
    "Tromsø": {"lat": 69.64, "lon": 18.95},
}

url = "https://api.met.no/weatherapi/locationforecast/2.0/compact?lat=63.43&lon=10.39"
response = requests.get(url)
print(response.json()['properties']['timeseries'][0]['data']['instant']['details']['air_temperature'])
print("-------------")
print(response.json())
print(response.json()['properties'])
print(response.json()['properties']['timeseries'][0])
print(response.json()['properties']['timeseries'][0].keys())
print(response.json()['properties']['timeseries'][0]['data'].keys())
print(response.json()['properties']['timeseries'][0]['data']['instant']['details']['air_temperature'])


def get_air_temp(lat, lon):
    url = "https://api.met.no/weatherapi/locationforecast/2.0/compact?lat={}&lon={}".format(lat, lon)
    response = requests.get(url)
    print(response.json()['properties']['timeseries'][0]['data']['instant']['details']['air_temperature'])


def get_air_temp_2(place):
    lat = places[f"{place}"]['lat']
    lon = places[f"{place}"]['lon']
    print(lat, lon)
    url = "https://api.met.no/weatherapi/locationforecast/2.0/compact?lat={}&lon={}".format(lat, lon)
    response = requests.get(url)
    print(response.json()['properties']['timeseries'][0]['data']['instant']['details']['air_temperature'])


#get_air_temp(59.91, 10.75)
#pprint(response.json())
#get_air_temp_2('Bergen')
