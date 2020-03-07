# python enumerate function
grocery = ['bread', 'milk', 'butter']
enumerateGrocery = enumerate(grocery)
print(list(enumerateGrocery))

# here enumerate function adds a counter to the
# each value in the list. counter will default starts
# from 0.
# when v print enumrated result v gets an enumerate object.
# so v converts it to list using list()
# counter is laike a key value for each iterator

# convert the enumerate object to tuple.
# sample -2
myGrades = ['A', 'B', 'C', 'D']
enumerateGrades = enumerate(myGrades)
print(tuple(enumerateGrades))

# can also add start value for the counter

laptop_brands = ['hp', 'dell', 'asus', 'samsung', 'haiti', 'xiaomi']
lapEnumerate = enumerate(laptop_brands, 2)
print(list(lapEnumerate))

# looping over an enumerated object
grocery = ['bread', 'milk', 'butter']
for item in enumerate(grocery):
    print(item)

print('\n')
for count, item in enumerate(grocery):
    print(count, item)

# here count represents the cpunter value

for count, item in enumerate(grocery, 100):
    print(count, item)

# Example
pages = ['page1', 'page2', 'page3', 'page4']
for c, i in enumerate(pages, 1001):
    print(c, i)
