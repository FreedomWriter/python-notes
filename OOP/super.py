# SUPER

class User():
    def __init__(self, email):
        self.email = email

    def sign_in(self):
        print('logged in')
    
    def attack(self):
        print('do nothing')

# this is all it takes to 'extend the prototype' Just give the sub-class the class you want to extend
class Wizard(User):
    def __init__(self, name, power, email):
        User.__init__(self, email) # USING PARENT CLASS
        self.name = name
        self.power = power

    def attack(self):
        print(f"Attacking with power of {self.power}")

class Archer(User):
    def __init__(self, name, num_of_arrows, email):
        super().__init__(email) # USING SUPER
        self.name = name
        self.num_of_arrows = num_of_arrows

    def attack(self):
        print(f"Attacking with arrows: arrows left -  {self.num_of_arrows}")

wizard1 = Wizard('Natalie', 'Hacking', "happy@hacking.com")
archer1 = Archer('Robin', 100, "hood@mail.com")

print(wizard1.email)