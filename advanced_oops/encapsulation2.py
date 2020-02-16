class Rectangle:
    def __init__(self, length, breadth, height):
        self.__length = length
        self.__breadth = breadth
        self.__height = height

    def set_length(self, len_value):
        self.__length = len_value

    def get_length(self):
        return self.__length

    def set_breadth(self, br_value):
        self.__breadth = br_value

    def get_breadth(self):
        return self.__breadth

    def set_height(self, hg_value):
        self.__height = hg_value

    def get_height(self):
        return self.__height

    def findVolume(self):
        return self.__length * self.__breadth * self.__height


vol1 = Rectangle(10, 5, 23)
print(vol1.findVolume())

vol1.set_length(4)
vol1.set_breadth(5)
vol1.set_height(5)

print(vol1.findVolume())
