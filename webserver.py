from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import quote, unquote
import json
import socket
import requests



def extract_json_string(string):
    start = string.find("{")
    stop = string.rfind("}")
    return string[start : stop + 1]


def get_ip_address():
    return socket.gethostbyname(socket.gethostname())


def dictionary_to_string(dictionary):
    return json.dumps(dictionary)


def json_string_to_dictionary(json_string):
    return json.loads(json_string)


def encode_string_into_url(string):
    return quote(string)


def decode_url_back_to_string(url_encoded_string):
    return unquote(url_encoded_string)


def string_to_unicode_bytes(string):
    return string.encode("utf-8")


class RequestHandler(BaseHTTPRequestHandler):
    def store_data(self, name, data):
        if not hasattr(self.server, "data"):
            self.server.data = {}
        self.server.data[name] = data
        print(11111, self.server.data)

    def load_data(self, name):
        if hasattr(self.server, "data"):
            if name in self.server.data:
                return self.server.data[name]
            else:
                return "Hello"
        return "Hai"

    def do_GET(self):
        # Phase 1: What has been requested?
        print("-------- Incoming GET request --------")
        print("  Request data: {}".format(self.requestline))

        # Phase 2: Which data do we want to send back?
        response = self.load_data('temperature')
        response1 = self.load_data('sensor_name')
        print(222, response)

        url = "https://api.met.no/weatherapi/locationforecast/2.0/compact?lat=63.43&lon=10.39"
        response2 = requests.get(url)
        response3 = str(response2.json()['properties']['timeseries'][0]['data']['instant']['details']['air_temperature'])

        print(response3, response)

        # Phase 3: Let's send back the data!
        response_in_bytes = string_to_unicode_bytes(response)
        response_in_bytes1 = string_to_unicode_bytes(response1)
        response_in_bytes2 = string_to_unicode_bytes(response3)

        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(response_in_bytes1)
        self.wfile.write(response_in_bytes)
        self.wfile.write(response_in_bytes2)
        print("done")

    def do_POST(self):
        # Phase 1: What has been requested?
        print("-------- Incoming POST request --------")
        print("  Request data: {}".format(self.requestline))
        post_data = decode_url_back_to_string(self.requestline)
        print(post_data)
        data1 = extract_json_string(post_data)
        print(data1)
        data1 = json_string_to_dictionary(data1)
        print(data1)
        print(data1['temperature'])

        self.store_data('temperature', data1['temperature'])
        self.store_data('sensor_name', data1['sensor_name'])


        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        print("2done")



port = 8023
httpd = HTTPServer(
    ("", port),
    RequestHandler,
)
print("")
print(" ******** TTM4175 Web Server  ******** ")
print(
    "    The server will be reachable via  http://{}:{}/".format(get_ip_address(), port)
)
print("    Terminate the server via Ctrl-C.")
print(" ************************************* ")
print("")
httpd.serve_forever()