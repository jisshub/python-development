# method overloading

class Employee:
    def __init__(self):
        pass

    def employeeInfo(self, name, age):
        return f"{name} and {age}"

    def employeeInfo(self):
        return "Great Employee"

    def employeeInfo(self, salary):
        return f"{salary}"


e1 = Employee()
print(e1.employeeInfo(4984))


# python deoesnt support method overloading since
# method argument don't have any types.


class Employee:
    def __init__(self):
        pass

    def employeeInfo(self, a):
        print(a)


a = Employee()
a.employeeInfo(34)
a.employeeInfo(True)
a.employeeInfo("jiss")

#
# A method accepting one argument can be called with an integer value, a string or a double
