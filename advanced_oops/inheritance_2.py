class Circle:
    def __init__(self, radius):
        self.__radius = radius
        self.pi = 3.14

    def get_radius(self):
        return self.__radius


class Area(Circle):
    def findArea(self):
        return f"Area: {round(self.pi * self.get_radius() * self.get_radius())}"


#
# s
class Circumference(Circle):
    def findCircum(self):
        return f"Circumference: {2 * self.pi * self.get_radius()}"


area = Area(6)
print(area.findArea())

peri = Circumference(7)
print(peri.findCircum())
