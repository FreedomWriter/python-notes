# FIRST GUI

#Display the image below to the right hand side where the 0 is going to be ' ', and the 1 is going to be '*'. This will reveal an image!

picture = [
  [0,0,0,1,0,0,0],
  [0,0,1,1,1,0,0],
  [0,1,1,1,1,1,0],
  [1,1,1,1,1,1,1],
  [0,0,0,1,0,0,0],
  [0,0,0,1,0,0,0]
]

for row in picture:
  for pixel in row:
    if(pixel == 1):
      print("*", end = "") # passing "" to end overides the default end which is a new line
    else:
      print(' ', end = "")
  print('') # need a new line after every row

fill = '$'
empty = ' '

for line in picture:
  for pixel in line:
    if(pixel):
      print(fill, end = "") # passing "" to end overides the default end which is a new line
    else:
      print(empty, end = "")
  print('') # need a new line after every row

# VANILLA CHECK DUPLICATES (does use built in method .count())

some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

duplicates = []
for value in some_list:
  if some_list.count(value) > 1:
    if value not in duplicates:
      duplicates.append(value)

print(duplicates)

print('\n############################################################################################\n')

# Exercise
#1. Wrap the above code in a function called checkDriverAge(). Whenever you call this function, you will get prompted for age. 
# Notice the benefit in having checkDriverAge() instead of copying and pasting the function everytime?

age = input("What is your age?: ")

def checkDriverAge(age):
  if int(age) < 18:
    return print("Sorry, you are too young to drive this car. Powering off")
  elif int(age) > 18:
    return print("Powering On. Enjoy the ride!");
  elif int(age) == 18:
    return print("Congratulations on your first year of driving. Enjoy the ride!")
checkDriverAge(age)

#2 Instead of using the input(). Now, make the checkDriverAge() function accept an argument of age, so that if you enter:
#checkDriverAge(92);
#it returns "Powering On. Enjoy the ride!"
#also make it so that the default age is set to 0 if no argument is given.

def checkDriverAge2(age=0):
  if int(age) < 18:
    return print("Sorry, you are too young to drive this car. Powering off")
  elif int(age) > 18:
    return print("Powering On. Enjoy the ride!");
  elif int(age) == 18:
    return print("Congratulations on your first year of driving. Enjoy the ride!")
checkDriverAge2(18)

print('\n############################################################################################\n')
