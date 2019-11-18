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
    location_part_1 = [os.path.splitext(x)[0] for x in json_filenames]
    newlist = list()
    # Iterate over mylist items
    for item in location_part_1:
        # split the element string into a list of words
        itemWords = item.split(",")

        print((item))
        # print(dict(itemWords))
        # extend newlist to include all itemWords
        newlist.append(itemWords)
    print(newlist)
    print("Processed" + str(location_part_1))
    keys = ['lat', 'lng']
    counter = 0
    array = []
    while counter < len(newlist):
        dictionary = dict(zip(keys, newlist[counter]))
        # print(dictionary)
        array.append(dictionary.copy())
        counter += 1
    # Closest to fixed array
    print("My Array" + str(array))
    print((array[1]))
    print("Fixed   " + str(tempDataList))
    print((tempDataList[1]))
    print("lats    " + str(item))
    # # Working json retrieval
    # print(closest(array, input))
    # matching_location = str(closest(array, input))
    # remove_part_1 = matching_location.replace("{'lat': ", '')
    # remove_part_2 = remove_part_1.replace(", 'lng':", ',')
    # file_output = remove_part_2.replace("}", '.json')
    # print(file_output)
    # with open('json/' + str(file_output)) as file:
    #     # need to send file name after getting closest
    #     api_data = json.load(file)
    # site_location = "lat :" + str(api_data["lat"] + ", lng : " + str(api_data["lng"]))
    # print(api_data)
    #
    # @app.route('/', methods=['GET'])
    # def api_all():
    #     return jsonify(api_data)
    #
    # app.run()


if __name__ == "__main__":
    main()
