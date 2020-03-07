# define a list

myList = [8, 9, 10, 20]

# get an iterator object using iter()
my_iter = iter(myList)
print(my_iter)

# to get the value representing that iterator
print(next(my_iter))

# next() to manualy get next value in iterator
print(next(my_iter))

print(next(my_iter))

# next(my_iter) is same as below
print(my_iter.__next__())

# will raise error.
print(my_iter.__next__())
