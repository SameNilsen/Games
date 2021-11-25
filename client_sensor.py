import requests
import json
from urllib.parse import quote, unquote


def dictionary_to_string(dictionary):
    return json.dumps(dictionary)

def encode_string_into_url(string):
    return quote(string)

def print_response(response):
    print('-------- Response --------')
    print('Status code: {}'.format(response.status_code))
    print('-------- Content--------')
    print(response.text)
    print('------------------------')

# example data
dictionary = {}
dictionary['temperature'] = '30.0'
dictionary['sensor_name'] = 'kitchen'

# ... your code ...
dictionary['temperature'] = encode_string_into_url(dictionary['temperature'])
dictionary['sensor_name'] = encode_string_into_url(dictionary['sensor_name'])
temp = dictionary_to_string(dictionary)
#temp = encode_string_into_url(temp)
print(temp)
response = requests.post('http://localhost:8023/?data={}'.format(temp))
print_response(response)
