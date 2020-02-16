class Students:
    def __init__(self, name, batch):
        self.__name = name
        self.__batch = batch

    def set_name(self, name_value):
        self.__name = name_value

    def get_name(self):
        return self.__name

    def set_batch(self, bt_value):
        self.__batch = bt_value

    def get_batch(self):
        return self.__batch


stud1 = Students('jiss', 'mca')
print(stud1.get_name())
print(stud1.get_batch())

stud1.set_name('adharsh')
print(stud1.get_name())

# cant access the private attribute outside the class
print(stud1.__name)

