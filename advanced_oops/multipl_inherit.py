class Birds:
    def __init__(self):
        self.feathers = True
        self.wings = True
        self.four_legs = False


class Flying:
    def fly(self):
        return 'they can fly'

    def speak(self):
        return 'Can Speak'


class Nonflying(Birds, Flying):
    def fly(self):
        return 'Cant Fly'


birds = Nonflying()
print(birds.feathers)
print(birds.wings)
print(birds.four_legs)

print(birds.fly())
print(birds.speak())
