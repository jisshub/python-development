# python working with json data

flightsData = {
    "passenger_id": 84694,
    "passenger_name": "jissmon",
    "ticKet_no": "DASD322",
    "date_flying": "12-03-2020",
    "health_problems": False,
    "accompaniers": [
        "jerin",
        "jibin",
        "dhrishya"
    ],
    "children": [
        {
            "firstName": "Alice",
            "Age": 33
        },
        {
            "firstName": "Bob",
            "Age": 22
        }
    ]
}

import json

# wrting json data to a file
with open("./extra_files/data1.json", "w") as jw:
    # use dump method to write to a json file,
    json.dump(flightsData, jw)


# reading from json file
with open("./extra_files/data1.json", "r") as jr:
    # read the contents in json file
    # f_cont = jr.read()
    # f_cont is a string object
    # load the json data using json method
    json_cont = json.load(jr)
    print(json_cont)
    # gets a dict type objec
    print(type(json_cont))

# using load method
# json.load() function which accepts a file object and does the f.read() part for you under the hood.
# here jr is a file pointer / fp
with open("./extra_files/data1.json", "r") as jr:
    json_Cont = json.load(jr)
    print(json_Cont)
    # access the values of each key
    print(json_Cont['passenger_id'])
    print(json_Cont['ticKet_no'])
