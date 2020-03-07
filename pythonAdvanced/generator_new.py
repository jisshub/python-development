# def myFunc():
#     n = 1
#     yield n
#     n += 1
#     yield n
#     n += 1
#     yield n
#
#
# a = myFunc()
# print(a.__next__())
# print(a.__next__())
# print(a.__next__())


# yield statement in for loop

def getAllData(grades):
    for each_Val in grades:
        yield each_Val


gradeList = [45, 66, 77, 99]
valOf = getAllData(gradeList)
print(valOf.__next__())
print(valOf.__next__())
print(valOf.__next__())
print(valOf.__next__())

# here v iterate through each value in iterable
