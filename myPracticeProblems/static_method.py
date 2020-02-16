# static method

class Training:
    def __init__(self, duration):
        self.duration = duration

    @staticmethod
    def trainerDetails(name, age, course):
        return f"{name}, {age}, {course}"


print(Training.trainerDetails("jissmon", 34, "python"))
