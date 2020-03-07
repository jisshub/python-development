# list slicing

myList = ["a", 4, True, "b"]
print(myList[1:])
print(myList[::1])
print(myList[::-1])

print(myList.append(5))
print(myList)

print(myList.extend([7, 3, 33]))
print(myList)

# delete/ remove from list
# del myList
print(myList)

# using remove method
print(myList.remove(True))
print(myList)

# pop method
print(myList.pop(4))
print(myList)

# index of value in list
print(myList.index(4))

# join method
first_name = ['jiss', 'aju', 'justin']
print("-".join(first_name))

print("$".join(first_name))

# list comprehensioon
list1 = [4, 5, 6, 8, 10, 30, 70]
print([nums for nums in list1 if nums > 9])
