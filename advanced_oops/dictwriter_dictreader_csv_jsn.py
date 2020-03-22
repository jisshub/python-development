# dict reader - dict writer - write to csv - read from csv
from csv import DictWriter, DictReader
import json

employeeDetails = [

    {"personId": 445,
     "personName": "jissmon",
     "profession": "software developer",
     "salary": 45000,
     "skills": [
         "python", "html/css", "javascript",
         "django"
     ]
     },
    {"personId": 245,
     "personName": "jerin",
     "profession": "software enginerr",
     "salary": 42000,
     "skills": [
         "mongoDB", "html/css", "javascript",
         "django"
     ]
     },
    {"personId": 415,
     "personName": "jaisil",
     "profession": "software developer",
     "salary": 45000,
     "skills": [
         "python", "html/css", "javascript",
         "django"
     ]
     },
]


# DictWriter
def write_to_csv():
    with open("./employee_data.csv", "w") as emp_csv:
        header = ["personId", "personName", "profession",
                  "salary", "skills"]
        csv_dict_obj = DictWriter(emp_csv, fieldnames=header)
        csv_dict_obj.writeheader()
        for employee_info in employeeDetails:
            csv_dict_obj.writerow(employee_info)


write_to_csv()


# Dict Reader
def read_from_csv():
    with open("./employee_data.csv", "r") as emp_csv:
        csv_dict_reader = DictReader(emp_csv)
        for read_each_row in csv_dict_reader:
            print(read_each_row)


read_from_csv()

# json write
with open("./employee_data.json", 'w') as json_dict:
    json.dump(employeeDetails, json_dict)

# json read
with open("./employee_data.json", 'r') as json_dict:
    json_dict_contents = json.load(json_dict)
    for read_data in json_dict_contents:
        print(read_data)
