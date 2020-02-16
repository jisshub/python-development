# oops
class Parrot:
    # class variable
    species = "bird"

    # instance variables
    def __init__(self, name, age):
        self.name = name
        self.age = age


obj = Parrot("blue", 22)
print(f"{obj.name} and {obj.age}, {Parrot.species}")
