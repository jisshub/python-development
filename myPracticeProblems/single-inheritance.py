# inheritance
class Department:
    College = "Fisat"

    def __init__(self, dname, rooms):
        self.dname = dname
        self.totalClassRoom = rooms

    def deptDetails(self):
        return f"{self.dname}, {self.totalClassRoom}, {Department.College}"


class Teachers(Department):
    TeacherName = "jiss"

    def teacherInfo(self):
        return f"{self.TeacherName}, {self.dname}"


class Student(Department):
    def studentInfo(self, studName):
        return f"{self.dname}, {self.totalClassRoom}, {studName}"


obj = Student("mca", 3)
print(obj.studentInfo("jisskhan"))
