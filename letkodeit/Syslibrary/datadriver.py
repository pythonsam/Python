"""
I have written a reusable function to extract the data from Json object.
We are making use of JSON object to keep all our data, which is much faster than Excel and xml
"""

import json


class readjson():
    def jsonread(self, filename):            # runtime will provide the file path
        with open(filename) as jsonfile:     # opens the json object
            value = json.load(jsonfile)      # converts json object into python object
            return value                     # returns value


