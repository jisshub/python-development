# generate random data - store - csv file
import random
from csv import writer
import json

names_1 = ["ajith", "john", "adharsh", 'justin', 'george',
           "abin", "corey", "jom", 'antony']
names_2 = ["kumar", "jose", "george", "vinay", "sourav", "kroos",
           "vishaal", "surya", "vijay", "edwin"]
place_list = ["angamaly", "kochi", "thrissur", 'kakkanad',
              "thevara", "kalady", 'seattle']


# storing in a csv file
# with open("./extrafiles/person.csv", "w") as csv_file:
#     write_to_csv = writer(csv_file)
#     write_to_csv.writerow(["first Name".upper(), "last name".upper(),
#                            "ssn".upper(), "age".upper(), "place".upper()])
#

class DummyClass:
    def __init__(self):
        # generate some dummy data
        self.first_name = random.choice(names_1)
        self.last_name = random.choice(names_2)
        self.ssn = random.randint(4242342342, 7897978987)
        self.age = random.randint(30, 51)
        self.place = random.choice(place_list)

    def need_all_infos(self):
        # storing in a csv file
        with open("./extrafiles/person.csv", "w") as csv_file:
            write_to_csv = writer(csv_file)
            write_to_csv.writerow(["first Name".upper(), "last name".upper(),
                                   "ssn".upper(), "age".upper(), "place".upper()])

            for count in range(10):
                # create a csv file and write data  to it.
                write_to_csv.writerow([self.first_name,
                                       self.last_name,
                                       self.ssn,
                                       self.age,
                                       self.place])

    # storing in json file
    def store_to_json(self):
        data_list = []
        # newDict = {}
        for count in range(10):
            # create a dictionary and add
            data_dict = dict(firstName=self.first_name,
                             lastName=self.last_name,
                             ssn=self.ssn,
                             Age=self.age,
                             Place=self.place)
            # append dict item in a list
            data_list.append(data_dict)
        # store into json file
        with open('./extrafiles/personData.json', "w") as pwr:
            json.dump(data_list, pwr)
        # read from a json file
        with open("./extrafiles/personData.json", "r") as pwr:
            json_contents = json.load(pwr)
            for all_data in json_contents:
                print('\n')
                print(all_data)


# create an instance
fileObj = DummyClass()
fileObj.need_all_infos()
fileObj.store_to_json()
