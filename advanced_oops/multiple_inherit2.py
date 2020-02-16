class Animal:
    def __init__(self):
        self.legs = True
        self.think = True


class Mammal:
    def backbones(self):
        return 'have backbones'

    def production(self):
        return 'produce milk'


class Human(Animal, Mammal):
    def speak(self):
        return 'Yes Can Speak'


h1 =Human()
print(h1.speak())
print(h1.backbones())
print(h1.production())
print(h1.legs)
print(h1.think)


