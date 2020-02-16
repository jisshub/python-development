# lambda functions

square = lambda x, y: x * y
print(square(4, 5))

# filter()
number = range(1, 20)
print(list(filter(lambda x: x % 2 == 0, number)))

# example -2
# using python function
salaryList = list()


def myList(salaries):
    return list(filter(lambda eachSal: eachSal > 5000, salaries))


while len(salaryList) < 5:
    newVar = int(input("Enter Salary: "))
    salaryList.append(newVar)
print(myList(salaryList))

# map method
names = ['jissmon', 'ajith', 'sachin']
print(map(lambda eachName: eachName.upper(), names))
# outputs a map object
