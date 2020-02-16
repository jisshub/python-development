class Cats:
    type = 'mammal'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        return f"{self.name},{self.age}, {self.type}"

    def find_oldest(self):
        if cat1.age > cat2.age:
            return f"{cat1.name} is elder than {cat2.name}"
        elif cat2.age > cat3.age:
            return f"{cat2.name} is elder than {cat3.name}"
        else:
            return f"{cat3.name} is elder than {cat2.name}"


cat1 = Cats('billy', 9)
cat2 = Cats('sulu', 5)
cat3 = Cats('kiran', 7)

print(cat1.show())
print(cat2.show())
print(cat1.find_oldest())
