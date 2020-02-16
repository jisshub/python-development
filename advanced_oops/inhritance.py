class Polygon:
    __width = None
    __height = None

    def set_values(self, width, height):
        self.__width = width
        self.__height = height

    def get_width(self):
        return self.__width

    def get_height(self):
        return self.__height


class Rectangle(Polygon):
    def area_rec(self):
        return self.get_height() * self.get_width()


class Triangle(Polygon):
    def area_tri(self):
        return .5 * self.get_width() * self.get_height()


rect = Rectangle()
rect.set_values(5, 6)
print(rect.area_rec())

tri = Triangle()
tri.set_values(8, 3)
print(tri.area_tri())
