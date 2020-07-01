# ABSTRACTION
## abstracting information and giving access to only what's necessary, everything else getss hidden under the hood.

class PlayerCharacter:
  def __init__(self, name='anonymous', age=0):
        self.name = name
        self.age = age
    

  def run(self): 
    print('run')
  
  def speak(self):
    print(f'My name is {self.name}, and I am {self.age} years old.')



player1 = PlayerCharacter('Natalie', 40)

# .speak() is an example of extraction - we don't know how it is being implemented when we call it, we just know it works
player1.speak() 