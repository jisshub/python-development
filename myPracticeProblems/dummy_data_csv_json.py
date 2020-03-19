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
with open("./extrafiles/person.csv", "w") as csv_file:
    write_to_csv = writer(csv_file)
    write_to_csv.writerow(["first Name".upper(), "last name".upper(),
                           "ssn".upper(), "age".upper(), "place".upper()])

    def need_all_infos():
        for count in range(10):
            # generate some dummy data
            first_name = random.choice(names_1)
            last_name = random.choice(names_2)
            ssn = random.randint(4242342342, 7897978987)
            age = random.randint(30, 51)
            place = random.choice(place_list)
            #       create a csv file and write data  to it.
            write_to_csv.writerow([first_name, last_name, ssn, age, place])


    need_all_infos()


# storing in json file
def store_to_json():
    data_list = []
    # newDict = {}
    for count in range(10):
        first_name = random.choice(names_1)
        last_name = random.choice(names_2)
        ssn = random.randint(4242342342, 7897978987)
        age = random.randint(30, 51)
        place = random.choice(place_list)
        # create a dictionary and add
        data_dict = dict(firstName=first_name, lastName=last_name,
                         ssn=ssn, Age=age, Place=place)
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


store_to_json()
