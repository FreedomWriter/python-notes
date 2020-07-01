# list, set, dictionary comprehensions
# comprehensions are a quick way to create the above data structures without looping or appending

my_list = []

for char in "hello":
    my_list.append(char)

print(my_list)

# simply looping over an iterable and creating a new list
my_list_comp = [char for char in 'hello from comprehension']
print (my_list_comp)
# creating a new list by looping over a range
my_list_range = [num for num in range(0,100)]
print(my_list_range)
# passing an expression and creating a new list by looping over a range
my_list_range_multiplied = [num*2 for num in range(0, 100)]
print(my_list_range_multiplied)
# passing an expression, creating a new list by looping over a range, adding a conditional
my_list_evens = [num**2 for num in range(0, 100)
  if num % 2 == 0]
print(my_list_evens)