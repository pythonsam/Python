"""
I have written reusable method to extract the data from JSON Object
We are making use of  JSON OBJECT to keep all our data, which is much faster than xml and xl
"""


import json


class ReadJson():
    def jsonread(self, filename):           # Runtime we will provide the File Path
        with open(filename) as jsonfile:    # Opens the Json Object
            value = json.load(jsonfile)     # converts the json object to python object
            return value                    # Returns Value




