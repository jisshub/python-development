class Person:
    def __init__(self, personName, personAge):
        self.name = personName
        self.age = personAge

    def showName(self):
        return self.name

    def showAge(self):
        return self.age


class Student:
    def __init__(self, studentid):
        self.studentid = 5833

    def showId(self):
        return self.studentid


class Residential(Person, Student):
    def completeDetail(self):
        return self.showName(), self.showAge()


new = Residential('john', 33)
print(new.completeDetail())

print(new.studentid)
