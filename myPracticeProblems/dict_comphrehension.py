# dictionary comprehension

names = ['jiss', 'akhil', 'manu']
rollNo = [30, 32, 34]
print({i: j for i in names for j in rollNo})

# example -1
numbers = {"first": 1, "second": 2, "third": 3}
print(numbers)

# using dict comprehension
print({key: value ** 2 for key, value in numbers.items()})

courseDict = dict(course1='bca', course2='mca', course3='bcom')
print({k: v.upper() for k, v in courseDict.items()})
