
class User():
    def sign_in(self):
        print('logged in')

# this is all it takes to 'extend the prototype' Just give the sub-class the class you want to extend
class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        print(f"Attacking with power of {self.power}")

class Archer(User):
    def __init__(self, name, num_of_arrows):
        self.name = name
        self.num_of_arrows = num_of_arrows

    def attack(self):
        print(f"Attacking with arrows: arrows left -  {self.num_of_arrows}")

wizard1 = Wizard('Natalie', 'Hacking')
archer1 = Archer('Robin', 100)

wizard1.sign_in()
archer1.sign_in()
wizard1.attack()
archer1.attack()

# isinstance(instance, Class)

print(isinstance(wizard1, Wizard))
print(isinstance(wizard1, User))
print(isinstance(wizard1, object)) # base class that python comes with - dunder methods are on the base `object` method