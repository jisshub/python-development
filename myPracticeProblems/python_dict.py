# dictionaries

# dict()

namesage = dict(name="jissmon", age=44)
print(namesage)

print(namesage["name"])

for each, each2 in namesage.items():
    print(each, each2)

# get values and keys
print(namesage.values())
print(namesage.keys())

# method
# fromkeys

myDict = {}.fromkeys(["name", "age", "marks"], ["jissmon", 55, [6, 5, 8]])
print(myDict)

print(namesage)

# adding new key:value pair to dictionary
namesage["marks"] = [56, 77]
print(namesage)


