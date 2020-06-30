#  @classmethod
# # @classmethods can be used without instantiating the cless, it is a method on the actual class
# ##  can use `cls` to instantiate an object in the method
#   @classmethod
#   def adding_things(cls, num1, num2):
#       return num1 + num2
# ##   @staticmethod behaves very similarly to @classmethod but does not give access to 'cls'

class PlayerCharacter:
  membership = True
  def __init__(self, name='anonymous', age=0):
        self.name = name
        self.age = age
    

  def introduce(self): 
    print(f'My name is {self.name}')
  
  def nick_name(self, nname):
    print(f'But you can call me {nname}')

  @classmethod
  def adding_things(cls, num1, num2):
      return  num1 + num2

player1 = PlayerCharacter('Natalie', 40)

print(player1.adding_things(17,27))
print(PlayerCharacter.adding_things(33,67)) # works because the method is on the class - not the object
# print(PlayerCharacter.introduce()) # will error out because nothing has been instqantiated


# ##  can use `cls` to instantiate an object in the method

class PlayerCharacterClassMethodInstatiate:
  membership = True
  def __init__(self, name='anonymous', age=0):
        self.name = name
        self.age = age

  def introduce(self): 
    print(f'My name is {self.name}')
  
  def nick_name(self, nname):
    print(f'But you can call me {nname}')

  @classmethod
  def adding_things(cls, num1, num2):
      return cls('Teddy', num1 + num2)
  @staticmethod # behaves very similarly to @classmethod but does not give access to 'cls'
  def adding_things(cls, num1, num2):
      return cls('Teddy', num1 + num2)

player3 = PlayerCharacterClassMethodInstatiate.adding_things(2,3)

print(player3.name, player3.age) 

