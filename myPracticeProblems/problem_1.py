# generate random data - store - csv file
import random
from csv import writer
import json

names_1 = ["ajith", "john", "adharsh", 'justin', 'george',
           "abin", "corey", "jom", 'antony']
names_2 = ["kumar", "jose", "george", "vinay", "sourav", "kroos",
           "vishaal", "surya", "vijay", "edwin"]

# ssn = range(3213213, 6867867)
age = range(30, 50)
place_list = ["angamaly", "kochi", "thrissur", 'kakkanad',
              "thevara", "kalady", 'seattle']

# storing in a csv file
with open("./extrafiles/person.csv", "w") as csv_file:
    write_to_csv = writer(csv_file)
    write_to_csv.writerow(["first Name".upper(), "last name".upper(),
                           "ssn".upper(), "age".upper(), "place".upper()])


    def need_all_infos():
        for count in range(10):
            first_name = random.choice(names_1)
            last_name = random.choice(names_2)
            ssn = random.randint(4242342342, 7897978987)
            age = random.randint(30, 51)
            place = random.choice(place_list)
            #       create a csv file and write data  to it.
            write_to_csv.writerow([first_name, last_name, ssn, age, place])


    need_all_infos()


# storing in json file

