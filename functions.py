# FUNCTIONS
## def signals the definition of a function
## syntax: 'def function_name():'

def say_hello():
  print('Hello World')

# say_hello()
tree = [
  [0,0,0,1,0,0,0],
  [0,0,1,1,1,0,0],
  [0,1,1,1,1,1,0],
  [1,1,1,1,1,1,1],
  [0,0,0,1,0,0,0],
  [0,0,0,1,0,0,0]
]
# # tree.reverse()
tree_icon = "T"
arrow_icon = "⬆"
def show_pic(pic, icon):
  print('')
  for row in pic:
    for pixel in row:
      if(pixel == 1):
        print(icon, end = "") # passing "" to end overides the default end which is a new line
      else:
        print(' ', end = "")
    print('') # need a new line after every row
  print('')

# postional arguments - arguments that must be in proper position
show_pic(tree, tree_icon)
show_pic(tree, arrow_icon)
show_pic(tree, tree_icon)

# keyword arguments - position doesn't matter (kind of introduces unneeded complexity)
show_pic(pic=tree, icon=tree_icon)

# default paramerters
def default_params(pic=tree, icon='S'):
  print('')
  for row in pic:
    for pixel in row:
      if(pixel == 1):
        print(icon, end = "") # passing "" to end overides the default end which is a new line
      else:
        print(' ', end = "")
    print('') # need a new line after every row
  print('')

# # default params provide a fallback in case no arguments are given to the function when invoked
# default_params()

# return

def sum(num1, num2): 
  return num1 + num2
total = sum(5,5)
# print(total)
# print(sum(total, total))

def nested_sum(num1, num2):
  def nest(n1, n2):
    return n1 + n2
  return nest(num1, num2)

# print(nested_sum(33,7))

# why would I do it like this???
def nested_sum(num1, num2):
  def nest(n1, n2):
    return n1 + n2
  return nest
nest_total = nested_sum(33, 67)
print(nest_total(33, 67))

# DOCSTRINGS
## lets you add comments to your functions, visible by the pop ups, the help fuction, or the magic (dunder) method function.__doc__
def test(a):
  '''
  Info: this function tets and prints param a
  '''
  print(a)

# help(test)
print(test.__doc__)

# *args & **kwargs
## both are banana words, but, you know, convention
## *args returns a tupple
## **kwargs returns a dict

# def super_func(*args, **kwargs):
#   print(type(args))
#   print(type(kwargs))
#   total= 0
#   for items in kwargs.values():
#     total += items
#   return sum(args) + total


print(super_func(1,2,3,4,5, num1=5, num2=10))

def super_func(name, *args, i='hi', **kwargs):
  print(type(args))
  print(type(kwargs))
  total= 0
  for items in kwargs.values():
    total += items
  return sum(args) + total

## RULE: params, *args, default parameters, **kwargs

print(super_func('Natalie', 1,2,3,4,5, num1=5, num2=10))
