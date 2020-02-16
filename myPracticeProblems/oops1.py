class Parrot:
    species = "Bird"

    def __init__(self, name, age):
        self.birdName = name
        self.birdAge = age

    # instance method
    def sing(self, song):
        return f"{self.birdName} sings {song}"

    def dance(self, colleague):
        return f"{self.birdName} dances with {colleague}"


# instantiate class
obj = Parrot("blue", 23)
print(obj.sing("shake it"))
print(obj.dance("arjun"))
