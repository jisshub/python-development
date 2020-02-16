class Food:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.discount = None

    def priceCheck(self):
        if self.price > 150:
            self.discount = 10
            self.price -= self.price * (self.discount / 100)
            return self.price
        else:
            return self.price


obj = Food('gilebi', 300)
print(obj.priceCheck())
