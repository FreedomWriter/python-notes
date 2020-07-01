
class User():
    def sign_in(self):
        print('logged in')
    
    def attack(self):
        print('do nothing')

# this is all it takes to 'extend the prototype' Just give the sub-class the class you want to extend
class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        User.attack(self) # USING THE ATTACK METHOD FROM USER
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

# POLYMORPHISM poly for many morphism for form
# # refers to the way object classes can share the same method name, but those method names can act differnetly based on whcih object calls it
# # the attack method in this example is a good demonstration of this

def player_attack(char):
    return char.attack()

player_attack(wizard1)
player_attack(archer1)

for char in [wizard1, archer1]:
    char.attack()