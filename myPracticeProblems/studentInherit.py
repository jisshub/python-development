# Example
class Person:
    def __init__(self):
        self.studentId = None
        self.firstName = None
        self.lastName = None
        self.scores = None


class Student(Person):
    scoresList = []
    getGradesDict = {'O': range(90, 100), 'E': range(80, 70),
                     'A': range(70, 80), 'P': range(60, 70)}

    def getStudentInfo(self):
        # global scoresList
        totalSubject = 5
        # get the student id
        self.studentId = input("Student Id: ")
        self.firstName = input("First Name: ")
        self.lastName = input("Last Name: ")
        while totalSubject > 0:
            self.scores = int(input("Your Score: "))
            self.scoresList.append(self.scores)
            totalSubject -= 1

    def printStudentInfo(self):
        # global scoresList
        print("**Details**")
        return f"Id: {self.studentId} \nName: {self.firstName} {self.lastName} \nscores: {self.scoresList}"

    def calculateAverage(self):
        avgOfScores = sum(self.scoresList) / len(self.scoresList)
        # global getGradesDict
        #       iterate thru gardes
        for grades, marks in self.getGradesDict.items():
            if avgOfScores in marks:
                return f"Grade: {grades}"


student = Student()
student.getStudentInfo()
print(student.printStudentInfo())
print(student.calculateAverage())
