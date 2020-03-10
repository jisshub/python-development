# divisibles
class First:
    def __init__(self):
        self.num = int(input("Enter Number: "))

    def checkDivisibles(self):
        myList = [1, self.num]
        for val in range(2, self.num):
            if self.num % val == 0:
                myList.append(val)
        return myList


obj = First()
print(obj.checkDivisibles())
