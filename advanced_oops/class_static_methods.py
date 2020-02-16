# class method and static method
# /class method is a methodon actual class
# in class method default parameter is cls instead of self.

class Cars:
    manufacturer = 'Skoda'

    # constructor / special method
    def __init__(self, model, engine):
        self.model = model
        self.engine = engine

    # instance method
    def fullDetails(self):
        return f"{self.model} and " \
               f"{self.engine}, {self.manufacturer}"

    @classmethod
    def givePrice(cls, price):
        return price

    @staticmethod
    def getAribag(status):
        return status

    def run(self):
        return self


car1 = Cars('octavia', '140kmpl')
print(car1.fullDetails())
print(car1.givePrice('3,50,000'))
# we can call the class method using class name
print(Cars.givePrice('35000'))


# static method
print(car1.getAribag(True))

# call using classname
print(Cars.getAribag(False))


#
print(car1.run())