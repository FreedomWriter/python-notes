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

# # Exercise
# #1. Wrap the above code in a function called checkDriverAge(). Whenever you call this function, you will get prompted for age. 
# # Notice the benefit in having checkDriverAge() instead of copying and pasting the function everytime?

# age = input("What is your age?: ")

# def checkDriverAge(age):
#   if int(age) < 18:
#     return print("Sorry, you are too young to drive this car. Powering off")
#   elif int(age) > 18:
#     return print("Powering On. Enjoy the ride!");
#   elif int(age) == 18:
#     return print("Congratulations on your first year of driving. Enjoy the ride!")
# checkDriverAge(age)

# #2 Instead of using the input(). Now, make the checkDriverAge() function accept an argument of age, so that if you enter:
# #checkDriverAge(92);
# #it returns "Powering On. Enjoy the ride!"
# #also make it so that the default age is set to 0 if no argument is given.

# def checkDriverAge2(age=0):
#   if int(age) < 18:
#     return print("Sorry, you are too young to drive this car. Powering off")
#   elif int(age) > 18:
#     return print("Powering On. Enjoy the ride!");
#   elif int(age) == 18:
#     return print("Congratulations on your first year of driving. Enjoy the ride!")
# checkDriverAge2(18)

# print('\n############################################################################################\n')

## CHALLENGE - write a function that takes a list as a paramater and returns the largest even number in the list

# my solution - 25 steps (is it worth the loss in readability) 
def highest_even(li):
  temp = 0
  for num in li:
    # could also be written as if not num % 2 - which would evaluate to Truthy or Falsy depending on whether it was a 0 or not - less readable
    if num % 2 == 0:
      temp = num if num > temp else temp
  return temp

print(highest_even([10,2,3,4,8,11, 99]))

# instructors solution
def other_highest_even(li):
  evens = []
  for num in li:
    if num % 2 == 0:
      evens.append(num)
  return max(evens)

print(other_highest_even([10,2,3,4,8,11, 20]))

print('\n############################################################################################\n')

# # PASSWORD CHECKER

# username = input('Enter username: ')
# password = input('Enter password: ')
# password_hidden = '*' * len(password)
# length = len(password)
# print(f'Hello, {username}, your password is {length} characters long.')

# print('\n############################################################################################\n')

#Given the below class:
class Kitty:
    species = 'mammal'
    def __init__(self, name, age):
        self.name = name
        self.age = age


# 1 Instantiate the Cat object with 3 cats
cat1 = Kitty('kitty', 1)
cat2 =Kitty('anotherkitty', 2)
cat3 = Kitty('oldestKitty', 3)

# 2 Create a function that finds the oldest cat
def find_oldest(*args):
  return max(args)

# 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2

print(f"The oldest cat is {find_oldest(cat1.age, cat2.age, cat3.age)} years old.")

print('\n############################################################################################\n')

# CHALLENGE

class Pets():
    animals = []
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'

class Simon(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Sally(Cat):
    def sing(self, sounds):
        return f'{sounds}'

#1 Add nother Cat
class Suzy(Cat):
    def sing(self, sounds):
        return f'{sounds}'

#2 Create a list of all of the pets (create 3 cat instances from the above)
my_cats = [Simon('Simon', 4), Sally('Sally', 21), Suzy('Suzy', 1)]

#3 Instantiate the Pet class with all your cats
my_pets = Pets(my_cats)

#4 Output all of the cats singing using the my_pets instance
my_pets.walk()

print('\n############################################################################################\n')

# CHALLENGE - CREATE A SUPERLIST

class SuperList(list):
  def __len__(self):
    return 1000

super_list1 = SuperList()
print(len(super_list1))
super_list1.append(5)
print(super_list1[0])
print(issubclass(SuperList, list))

print('\n############################################################################################\n')

# LAMBDA CHALLENGES

# #CREATE A LAMBDA EXPRESSION TO SQUARE A LIST

my_list = [5,4,3]
new_list = list(map(lambda item: item * item, my_list))
print(new_list)

# # LIST SORTING
## sort the following list of tuples by the second key

a= [(0,2), (4,3), (9,9), (10, -1)]
# .sort() takes a key as it's first param
# # here we are using a lambda expression to assign the key at the index of 1 in each tuple to the key being given to sort
a.sort(key=lambda x: x[1])

print('\n############################################################################################\n')

# CHALLENGE - CREATE A LAMBDA FUNCTION THAT RETURNS A LIST OF ANY DUPLICATE VALUES IN A GIVEN LIST. EACH ITEM IN THE LIST SHOULD BE UNIQUE

some_list_2 = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

# Step 1 - declarea variable
## duplicates2 = [x]
# Step 2 - loop over list
## duplicates = [x for x in some_list_2 ]
# Step 3 - add a conditional that checks the number of occurances of x in the given list and returns items with occurances greater than 1
## duplicates = [x for x in some_list_2 if some_list_2.count(x) > 1]
# Step 4 - convert that list to a set to remove duplicate entries
## duplicates = set([x for x in some_list_2 if some_list_2.count(x) > 1])
# Step 4 - convert set back to a list
## duplicates = list(set([x for x in some_list_2 if some_list_2.count(x) > 1]))

duplicates2 = list(set([x for x in some_list_2 if some_list_2.count(x) > 1]
))
print(duplicates2)

print('\n############################################################################################\n')

# Create an @authenticated decorator that only allows the function to run is user1 has 'valid' set to True:
user1 = {
    'name': 'Sorna',
    'valid': True
}

def authenticated(fn):
  def wrapper(*args, **kwargs):
    if args[0]['valid']:
        return fn(*args, **kwargs)
  return wrapper

@authenticated
def message_friends(user):
    print('message has been sent')

message_friends(user1)

print('\n############################################################################################\n')

# # # Guessing game, WON'T WORK BEING RAN FROM THIS FILE - COPY PASTE INTO A NEW FILE OR REPL.IT

# # generate a number 1-10
# # get imput from user
# # check that input is a number 1-10
# #check if number is the right guess. Otherwise aqsk again

# from random import randint

# answer = randint(1,10)

# # to give paramaters while running program in a terminal (negating the need for an input)
# # # comment out lines 8 and 16, then uncomment following lines:


# # import sys

# # answer = (randint(int(sys.argv[1]),int(sys.argv[2])))


# while True:
#     try:
#         guess = int(input('guess a number 1~10: '))
#         # if int(guess) > 1 and int(guess) < 11:
#         if 0 < guess < 11:
#             if guess == answer:
#                 print('you are a genious')
#                 break
#         else: 
#             print("c'mon, 1~10 buddy")
#     except ValueError:
#         print('Please enter a number')
#         continue

print('\n############################################################################################\n')
