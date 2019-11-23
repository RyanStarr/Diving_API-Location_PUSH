import json

from flask import Flask
from flask_restful import Api, Resource

# Setup REST API
app = Flask(__name__)
api = Api(app)


def file_name(latlng):
    # Split latitude and longitude
    lat = str(latlng).split(',')[0]
    lng = str(latlng).split(',')[1]
    # Round to 2 decimal places
    simple_lat = round(float(lat), 2)
    simple_lng = round(float(lng), 2)
    # Combine simplified back together
    simple_latlng = str(simple_lat) + ',' + str(simple_lng)
    return simple_latlng


def get_json(name):
    # Open matching location file
    try:
        with open(name + '.json') as file:
            # Read file contents
            api_data = json.load(file)
    except:
        api_data = "Location not found", 404
    return api_data


class Data(Resource):
    def get(self, latlng_input):
        # Get latitude and longitude from GET request.
        try:
            json_data = get_json(file_name(latlng_input))
        except:
            json_data = "Failed to extract location"
        # Output retrieved data.
        return json_data

# Example GET request http://127.0.0.1:5000/location/-29.0238,167.9082
api.add_resource(Data, "/location/<string:latlng_input>")

#app.run(debug=True)
