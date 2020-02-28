# exceptions
myList = [5, 6, 7, 8]

try:
    # list index out of range
    print(myList[6])
    print("hello")
except Exception as e:
    print(myList[0:])
    print(e.args)

finally:
    print("Execute First")


# example

def exceptFun(numbers):
    try:
        numbers.append(5, 6, 7)
    except Exception as e1:
        numbers.append(4)
        print(e1.args)
    finally:
        print(numbers)


exceptFun([10, 30, 20, 50])


