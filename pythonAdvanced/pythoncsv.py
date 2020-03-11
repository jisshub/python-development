# reading and writing from/to csv
# use reader()
import csv
with open("./extra_files/final.csv", "r") as csv_file:
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        print(row)
        # get a list type
        print(row[1])
#         get just first index value


# to read the csv data to a dictionary
# use DictReader
import csv
with open("./extra_files/final.csv", "r") as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        print(row)
        # get a dict type data
        print(row["Name"])
        # get just name values




