# Python doesn't have true private variables
## we make up for it by using _variable_name as a naming convention (single underscore, NEVER double)
## this signals to other devs, that a variable shouldn't be touched

class PlayerCharacter:
  def __init__(self, name='anonymous', age=0):
        self._name = name
        self._age = age
    

  def run(self): 
    print('run')
  
  def speak(self):
    print(f'My name is {self._name}, and I am {self._age} years old.')



player1 = PlayerCharacter('Natalie', 40)

