class Employee:
    def __init__(self, name):
        self.name = name
        # private variables
        self.__empId = None
        self.__empSal = None

    # setter method to set value to private variable empid
    def setEmpId(self):
        self.__empId = 947239

    # getter method to get values from private variable
    def getEmpId(self):
        return f"Employee Id: {self.__empId}"

    def setEmpSal(self):
        self.__empSal = 50000

    def getEmpSal(self):
        return f"Employee Salary:  {self.__empSal}"


# #
# class NewEmp(Employee):
#     def printInfo(self):
#        self.e

obj = Employee("jissmon")
# invoke the setter and getter methods on instance
obj.setEmpId()
print(obj.getEmpId())
obj.setEmpSal()
print(obj.getEmpSal())
print(obj.name)
