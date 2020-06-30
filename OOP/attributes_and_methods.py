class PlayerCharacter:
  # CLASS OBJECT ATTRIBUTE - static, not dynamic
  membership = True
  def __init__(self, name='anonymous', age=0):
    #   if (PlayerCharacter.membership): # this syntaz would work as well
    if (age > 18):
        # these attrs are not class object attributes, they are constructor defined, dynamic, and specific to each instqance
        self.name = name # ATTRIBUTE
        self.age = age
    else: 
        print('Must be over 18 to play')
    

  def introduce(self): # METHOD
    print(f'My name is {self.name}')
  
  def nick_name(self, nname): # METHOD
    print(f'But you can call me {nname}')

player1 = PlayerCharacter('Natalie', 40)
player2 = PlayerCharacter('Chomsky', 1.5)

player1.attack = "Fight the power!" # can assign methods using dot notation

print(player1.membership)
print(player1.name)
print(player1.introduce())
print(player1.nick_name('Freedom Writer'))
# print(player2.name) # will error out, player 2 isn't old enough and therefore it's name is never instantiated