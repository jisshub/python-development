# list comprehension
# get employee starting with s

empNames = ['sehwag', 'sachin', 'ajith', 'justin']
print([eachEmp for eachEmp in empNames if eachEmp[0] == 's'])

# remove all vowels in string

print([eachChar for eachChar in 'jissmon' if eachChar not in 'aeiou'])

# list comprehension vs for-loop

# using for loop
letterList = list()
for eachLetter in 'human':
    letterList.append(eachLetter)
print(letterList)

# method-2
print([eachLetter for eachLetter in "human"])

# using list comprehension for nested for loop
list1 = ['a', 'b', 'c', 'd']
list2 = [10, 20, 30, 40]
print([(i, j) for i in list1 for j in list2])
