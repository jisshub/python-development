# generators in python
def myFunction():
    yield "a"
    yield "b"
    yield "c"


x = myFunction()

# use next() or __next__() to get the value returned by yield
print(x.__next__())
# gets the next value of yield.
print(x.__next__())
# gets the next value of yield
print(x.__next__())
# get next value - StopIteration error rises -since no more value to yield.
print(next(x))

# at a time it yields a single iterator object


# here when v call thefucntion, fucnction execites frist iterator given in yield
# and this yield pause and save the function current state.
# when v call the next() method again, it execuets next yield, it goes until last yield statement

