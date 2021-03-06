# Methods
  # methods are invoked by dot notation, keyword, ()
  # .format()
  # on the class they belong to

quote = "to be or not to be"

print(f'quote = "to be or not to be"\n')

print(f'print(quote.upper()):\n  # prints {quote.upper()}\n')

print(f'print(quote.find("be")):\n  # prints "{quote.find("be")}", which is the position in which it finds the index in which begins the first occurance \n')

# print(f'print(quote.replace("be", "me")):\n \n # prints "{quote.replace("be", "me")}":# repalcing all occurances of the first value with the second value\n # not permananent - strings are immutable\n # .replace() actually creates a new value wich can be assigned to mememory\n')

print(f'print(quote.capitalize()):\n  # prints "{quote.capitalize()}"\n')


print('\n############################################################################################\n')

# More Built In Functions
  # Built in functions has the syntax of a keyword followed by ()

# len() is not zero indexed

print(f'print(len("What is the length of this string?"))\n  # prints: {len("will print the length of this string")}\n')

greet = 'hello!!!'

print('greet = hello!!!\n')

print(f'print(greet[0:len(greet)]))\n  # prints: {greet[0:len(greet)]} where greet = "hello!!!"')


print('\n############################################################################################\n')


# BOOLEANS - note capital T & F

print(f'bool(1) evaluates to {bool(1)}')
print(f'bool(0) evaluates to {bool(0)}\n')


print('\n############################################################################################\n')