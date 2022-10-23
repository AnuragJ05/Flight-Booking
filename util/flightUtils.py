import json
from flask import request


def get_flight_details():
    if request.method == "GET":
        with open('config/flight.json') as json_file:
            data = json.load(json_file)
        return data
