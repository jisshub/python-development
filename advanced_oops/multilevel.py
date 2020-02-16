class Birds:
    def __init__(self):
        self.feathers = True
        self.wings = True
        self.legs = False


class Flying(Birds):
    def fly(self):
        return 'Can Fly'

    def hunt(self):
        return 'Can Hunt'


class Nonflying(Flying):
    def speak(self):
        return 'Can Speak'

    def fly(self):
        return 'Can Fly'


new = Nonflying()
print(new.feathers)
print(new.wings)
print(new.legs)

print(new.speak())
print(new.fly())
print(new.hunt())

