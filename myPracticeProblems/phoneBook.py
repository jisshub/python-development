# problem 3
class MyPhoneBook:
    def __init__(self):
        self.limit = None
        self.dict = dict()

    def addPhones(self):
        self.limit = int(input("Enter total: "))
        while self.limit > 0:
            user_name = input("Enter user name: ")
            self.dict[user_name] = int(input("Enter Phone: "))
            self.limit -= 1
        return self.dict

    def QueryTheName(self):
        name = input("Enter Name: ")
        if name in self.dict.keys():
            return f"{name}={self.dict[name]}"
        else:
            return "not found"


phone_obj = MyPhoneBook()
print(phone_obj.addPhones())
print(phone_obj.QueryTheName())
