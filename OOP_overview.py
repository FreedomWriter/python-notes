# # OOP
# ## Everything in python is an object, with different compile
# ## Objects have methods and attributes that you can access with dot notation

print(type(None))
print(type(True))
print(type(False))
print(type(5))
print(type(5.5))
print(type('hi'))
print(type([]))
print(type({}))
print(type(()))


# # Creating a class
# ## a class is the blueprint of what we want to create
# ## Naming convention is to capitalize and camelCase
# ## classes can be instantiated to create different instances which are known as objects

class BigObject: # class
  #write the code
  pass

print(type(BigObject))

# # type(BigObject) will return class because we haven't actually created the object yet, just the class")

# # creating the object
# ## the object is an instance of the class
# ## the properites, attributies and methods of the class are extended to the object

obj1 = BigObject() # instanciate
print(type(obj1))

# Example:
## __init__ is a dunder method (aka magic method) and is automatically called each time a new instance is instanciated

class PlayerCharacter:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def run(self):
    print('run')
  

player1 = PlayerCharacter('Natalie', 40)
player2 = PlayerCharacter('Chomsky', 1.5)

player1.attack = "Fight the power!" # can assign methods using dot notation

print(player1.name)
print(player2.name)
print(player2.run())

print(player1.attack)
