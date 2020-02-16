class Hello:
    def __int__(self):
        self.__c = 40

    def public_method(self):
        print('public method')
        # print(self.__c)
        # can access the private with in the class
        return self.__private_method()

    def __private_method(self):
        print('private')


hello = Hello()
hello.public_method()
# cant call the private method outside the class
hello.__private_method()


