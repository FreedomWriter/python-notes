# list, set, dictionary comprehensions
# comprehensions are a quick way to create the above data structures without looping or appending

# instead of:
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

my_set = []

for char in "hello":
    my_set.append(char)

print(my_set)

# simply looping over an iterable and creating a new set
my_set_comp = {char for char in 'hello from comprehension'}
print (my_set_comp)
# creating a new set by looping over a range
my_set_range = {num for num in range(0,100)}
print(my_set_range)
# passing an expression and creating a new set by looping over a range
my_set_range_multiplied = {num*2 for num in range(0, 100)}
print(my_set_range_multiplied)
# passing an expression, creating a new set by looping over a range, adding a conditional
my_set_evens = {num**2 for num in range(0, 100)
  if num % 2 == 0}
print(my_set_evens)

simple_dict = {
    'a': 1,
    'b': 2
}
my_dict = { key:value**2 for key,value in simple_dict.items() }


my_dict_comp = { key:value**2 for key,value in simple_dict.items() }
print (my_dict_comp)

my_dict_evens = {k:v**2 for k,v in simple_dict.items()
  if v % 2 == 0}
print(my_dict_evens)

# creating a dic from a list where the key is equal to the number from the list and the value is equal to the number from the list times two
my_dict_from_list = {num:num * 2 for num in [1,2,3]}
print(my_dict_from_list)