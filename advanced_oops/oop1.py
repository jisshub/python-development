class PlayerCharacter:
    # class attrbiute - doesnt change for the instances. all instances hav same class attribute
    company_name = 'Fingent'

    def __init__(self, name, experience, job):
        # instance attribute - it is dynamic, ie it may change for each instance
        self.name = name
        self.exp = experience
        self.job = job

    # def saal

    def detail(self):
        return f"name: {self.name}, experience:{self.exp}, " \
               f"job: {self.job}, company: {self.company_name} "


player1 = PlayerCharacter('jissmon jose', 6, 'software developer')
# here self refers to player1
print(player1.detail())

# here self refers to player2

# init is a constructor which runs everytime when
# v create an object. player1 is the object.

# self refers to the current object. it is a default parameter.

# if self not used, throws attribute error.

# here v can create different players with attributes, but just need same code.
# thus oops satsfy the dry principle.


# here name, experience, job are attributes player1 posses.

# can also call class attribute using the class name.

