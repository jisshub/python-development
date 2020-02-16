# Given the names and grades for each student in a Physics class of  students, store them in a nested list
# and print the name(s) of any student(s) having the second lowest grade.

namesGrades = [['jissmon', 20], ['ajith', 50], ['nikhil', 40]]
print(namesGrades)

print(namesGrades[2][0])

# print(namesGrades[1])
# print(type(namesGrades))
# GradesList = list()
# studentList = list()
# for eachName in namesGrades:
#     # print(f'Student Name: {eachName[0]}, Grade: {eachName[1]}')
#     GradesList.append(eachName[1])
#     studentList.append(eachName[0])
# print(GradesList)
# print(studentList)
# var = sorted(GradesList)[-2]


# using dictionary comprehension
var1 = {each[0]: each[1] for each in namesGrades}
print(var1)
# print(var1.get("ajith"))


valueList = list()
keyList = list()
for key, value in var1.items():
    valueList.append(value)
    keyList.append(key)

print(valueList)
secValue = sorted(valueList)
print(secValue)
print(secValue.index(secValue[-2]))

# make a list of keys
# print(keyList[secIndex])

# print(valueList.index(secValue))
