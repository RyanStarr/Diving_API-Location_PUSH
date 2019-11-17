from flask import Flask, jsonify
import json, os
from math import cos, asin, sqrt

app = Flask(__name__)
app.config["DEBUG"] = True


# # ------Calculate closest location------------
def distance(lat1, lon1, lat2, lon2):
    p = 0.017453292519943295
    a = 0.5 - cos((lat2 - lat1) * p) / 2 + cos(lat1 * p) * cos(lat2 * p) * (1 - cos((lon2 - lon1) * p)) / 2
    return 12742 * asin(sqrt(a))


def closest(data, input):
    # return min(data, key=lambda p: distance(input['lat'], input['lng'], p['lat'], p['lng']))
    return min(data, key=lambda p: distance(input['lat'], input['lng'], p['lat'], p['lng']))


# # -------------------------------------------

tempDataList = [{'lat': 39.7612992, 'lng': -86.1519681},
                {'lat': 39.762241, 'lng': -86.158436},
                {'lat': 39.7622292, 'lng': -86.1578917}]


def main():
    input = {'lat': -28.9913, 'lng': 167.9249}


    # Retrieve files and strip them of ".json" ending.
    json_path = 'json/'
    json_filenames = [pos_json for pos_json in os.listdir(json_path) if pos_json.endswith('.json')]

    # Add in formatting to list of locations
    # location_part_1 = ["{'lat': " + os.path.splitext(x)[0] + "}" for x in json_filenames]
    location_part_1 = [os.path.splitext(x)[0] for x in json_filenames]
    # location_part_1 = [os.path.splitext(x)[0] for x in json_filenames]
    location_part_2 = (a.split(",") for a in location_part_1)

    # location_part_3 = [i.replace(',', ", 'lng': ") for i in location_part_2]
    # for key, value in location_part_1.it
    print("GETTNG DATA")
    # print("Temp one item" + str(tempDataList[1]))
    print("Temp    " + str(type((tempDataList[0]))))
    print("Final   " + str(list(location_part_2)))
    print("GOT DATA")


#  dictOfWords = {i: location_part_1[i] for i in range(0, len(location_part_2))}
# print(dictOfWords)
# # print("Location" + str(locations))
# print("Get data")

# # Working json retrieval
# print(closest(tempDataList, input))
# matching_location = str(closest(tempDataList, input))
# remove_part_1 = matching_location.replace("{'lat': ", '')
# remove_part_2 = remove_part_1.replace(", 'lng':", ',')
# file_output = remove_part_2.replace("}", '.json')
# print(file_output)
# with open('json/' + str(file_output)) as file:
#     # need to send file name after getting closest
#     api_data = json.load(file)
# site_location = "lat :" + str(api_data["lat"] + ", lng : " + str(api_data["lng"]))
# print(api_data)

# @app.route('/', methods=['GET'])
# def api_all():
#     return jsonify(api_data)
#
# app.run()


if __name__ == "__main__":
    main()
