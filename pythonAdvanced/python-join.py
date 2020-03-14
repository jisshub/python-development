# python- break

personData = [{"name": "jissmon", "sex": "Male"}, {"name": "Ajitha", "sex": "Female"},
              {"name": "jerin", "sex": "Male"}]

for eachData in personData:
    # print(eachData)
    for name, sex in eachData.items():
        if eachData["sex"] == "Male":
            print("Mr." + " " + eachData["name"])
            break
        print("Ms." + " " + eachData["name"])
        break

# here if sex is male, conact Mr with name and break that inner for loop - to avoid looping that
# same dictionary item - thus iteration backs to the outer loop.

# similar in case of Female. if sex is female. terminate the inner loop and returns
# to outer for loop




