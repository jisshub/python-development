# method overriding

class Student:
    def __init__(self, name, rollNo):
        self.name = name
        self.rollNo = rollNo

    def admnData(self):
        admnNo = 93802
        return admnNo, self.name, self.rollNo


class NewStudent(Student):
    def admnData(self):

        # here v call the parent class method from child class usng super()
        print(super().admnData())
        admnNo = 4863278
        print(admnNo, self.name, self.rollNo)


obj = NewStudent("jissmon", 45)
print(obj.admnData())

# method overriding is possible in python
