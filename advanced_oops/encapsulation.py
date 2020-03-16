# encapsulation
# binding of data & functions that manipulates the data
class Cars:

    def __init__(self, model, speed, color):
        self.model = model
        self.__speed = speed
        self.__color = color

    # setter
    def set_speed(self, value):
        self.__speed = value

    # getter
    def get_speed(self):
        return self.__speed

    def set_color(self, new_value):
        self.__color = new_value

    def get_color(self):
        return self.__color


car1 = Cars('Ford', 200, 'blue')
print(car1.get_speed())
car1.set_speed(500)

# __speed is a private attribute so , it cant be manipulated using object .
car1.__speed = 550
print(car1.get_speed())

# model is a public attribute by default
car1.model = 'bmw'
print(car1.model)


# __color is a private attribute
print(car1.get_color())
car1.set_color('green')
print(car1.get_color())
