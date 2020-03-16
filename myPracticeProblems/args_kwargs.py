def print_all(*args, status):
    return f"{args}\n{status}"


try:
    getIn = print_all(4, 6, 7, 7, 8, status="active")
    print(getIn)
except TypeError as e:
    print(e.args)


# note: arguments after the args should be given specified as keyword
# arguments
# keyword and parameter must be same


# kwargs
# regular paramets should comes at first not after kwargs
def getkwargs(class_room, **kwargs):
    for key, value in kwargs.items():
        print(key, value)
    print(class_room)


try:
    # pass the arguments a keywords arguments
    getkwargs("first floor", name="jismon", age=44, marks=0, grade="A")

except Exception as e:
    print(e.args)
