from flask import Flask
from flask_restful import Api, Resource, reqparse
import json, os
app = Flask(__name__)
api = Api(app)

locations = [
    {
        "name": "Elvin",
        "age": 32,
        "occupation": "Doctor"
    }
]


def file_name(latlng):
    lat = str(latlng).split(',')[0]
    lng = str(latlng).split(',')[1]
    simple_lat = round(float(lat), 2)
    simple_lng = round(float(lng), 2)
    simple_latlng = str(simple_lat) + ',' + str(simple_lng)
    return simple_latlng
    #with open(latlng + '.json') as file:
     #   api_data = json.load(file)
    #return api_data

def get_json(file_name):
    with open(file_name + '.json') as file:
        api_data = json.load(file)
# site_location = "lat :" + str(api_data["lat"] + ", lng : " + str(api_data["lng"]))
    print(api_data)
    return api_data

class Data(Resource):
    def get(self, latlng_input):
        print("Original" + str(latlng_input))
        print("File name" + str(file_name(latlng_input)))
        json_data = get_json(file_name(latlng_input))
        return json_data


        # for location in locations:
        #     if (latlng_input == location["name"]):
        #         return location, 200
        # return "Location not found", 404


api.add_resource(Data, "/location/<string:latlng_input>")

app.run(debug=True)
