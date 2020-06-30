# SCOPE
## Python has functional scoping (as well as global)
## if statements do not create their own scope
## Scope rules the python interpreter follows
### local
### parent local
### global
### built in function

if True:
  x = 10

print(x) # x is available (in the global scope)

some_list = ["oh","hello",'world']


for word in some_list:
 word.capitalize()

print(word) # word is available (in the global scope) - will be the last iteration, not the whole list

# GLOBAL KEYWORD
## gives access to a global variable within the function scope

total = 0 
def count():
  global total
  total += 1
  return total

print(count())
print(count())
print(count())

# DEPENDENCY INJECTION

def dep_count(total):
  total
  total += 1
  return total

print(dep_count(dep_count(dep_count(total)))) # need to nest this way to get a cumalitve total, otherwise, invoking multiple instances of dep_count(total) returns 1 as the work done within the function gets lost with each invoction
print(dep_count(total))
print(dep_count(total))

# NONLOCAL - used to refer to parent local

def outer():
  x  = 'local x'
  def inner():
    # nonlocal x # declare intention to use parent scope
    # # x = 'reassigned x' # this line reassigns the value of x (assuming `nonlocal x` has been declared) in both parent and child scope
    print("child: ", x)

  inner()
  print("parent: ", x)

print(outer())

print("Hello" == "Hello")