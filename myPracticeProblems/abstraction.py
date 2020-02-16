# abstraction
from abc import abstractmethod


class JobInterview:
    company = "netsrratum"

    def __init__(self, date, time):
        self.date = date
        self.time = time

    # declare an abstract method
    @abstractmethod
    def print(self):
        pass


class Candidate(JobInterview):
    # here v implement the abstract method
    def print(self):
        candidateName = input("Enter Name: ")
        return f"{self.date} and {self.time} and {candidateName}"


c1 = Candidate('10-4-2020', '11:30')
print(c1.print())
