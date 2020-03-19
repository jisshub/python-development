import json

personData = {
    "eachData": [
        {
            "firstName": "jissmon",
            "lastName": "jose",
            "ssn": 4234234234,
            "age": 33,
            "place": "angamaly"
        },

        {
            "firstName": "justin",
            "lastName": "jose",
            "ssn": 4234234234,
            "age": 33,
            "place": "angamaly"

        }

    ]
}

# write
with open("./extrafiles/personDataSample.json", "w") as jw:
    json.dump(personData, jw)
# read
with open('./extrafiles/personDataSample.json', "r") as jr:
    json_cont = json.load(jr)
    get_each_ONE = personData.get("eachData")
    for all_data in get_each_ONE:
        print("\n")
        for key, value in all_data.items():
            print(f'{key}: {value}')
