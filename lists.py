# LISTS
## list is an ORDERED sequence of objects of any type.
## lists are zero indexed
## lists can be sliced [start:stop:stepover] -  slicing creates a new list, the original will remain untouched
# # lists are mutable so you can assign values by specifiying the index position you want the new value to hold.
# # assigning a new space in memory by declaring a new variable lets us mutate the value of the new variable, which is a copy of the original list,  without affecting the value stored in memory for the original list

print('#LISTS\n## lists are ORDERED sequences of objects of any type.\n## lists are zero indexed\n## lists can be sliced [start:stop:stepover] -  slicing creates a new list, the original will remain untouched\n## the value of the list slice can be assigned to a new variable\n##  assigning a list to a new variable without slicing will result in both variable pointing to the same space in memory. Any change to the list via one variable will reflect those changes in the other variable')

print("\n# VALID LIST FORMATS\nli = [1,2,3,4,5,]\nli2 = ['a', 'b', 'c']\nli3 = [1,2,'a', True]\n")
# li = [1,2,3,4,5,]
# li2 = ['a', 'b', 'c']
# li3 = [1,2,'a', True]

# LIST SLICING 
#
amazon_cart = [
  'notebooks',
  'sunglasses',
  'toys',
  'grapes'
]
# 
amazon_cart[0] = "new_value"
new_cart = amazon_cart[0:3]
new_cart[0] = "gum"
print(f"amazon_cart: ['notebooks', 'sunglasses', 'toys', 'grapes']\n")
print(f"# print(amazon_cart[0]) ----> notebooks\n")
print("amazon_cart[0] = 'new_value'")
print(f'# print(amazon_cart[0]) ----> {amazon_cart[0]}\n')
print('new_cart[0] = "gum"')
print(f"#print(new_cart) ----> {new_cart}\n")
print(f"#print(amazon_cart) ----> {amazon_cart}\n")
print('new_cart = amazon_cart[0:3] # new_cart = amazon_cart[0:3] ---->  {new_cart = amazon_cart[0:3]}')




print('\n############################################################################################\n')


# MATRIX
## a way to describe mulit-dimensional lists
## simplified to a list with another list inside of it
## matrix is a banana word but most devs will expect to see 'matrix'

matrix = [
  [1,"second item, first list",3],
  [2,4,6],
  [7,8,9]
]

print(f"# MATRIX\n## a way to describe mulit-dimensional lists\n## simplified to a list with another list inside of it\n## matrix is a banana word but most devs will expect to see 'matrix'")
print(f'print(matrix[0][1]) ----> {matrix[0][1]}\n')

# LIST METHODS
## ADDING
### .append(), .insert(), .extend() - changes the list 'in place' it doesn't produce a value (no return value)
####  this means we have to 'append before we assign'
### .insert() - takes two params. The first is the index  to insert, the second is the value (object) to insert

basket = [1,2,3,4,5,]
basket.append(100)
new_list = basket

print(f"#len() --- a function, not a method\n # len(list_name) will give the length of the list assigned to the list_name variable\n")
print('basket = [1,2,3,4,5,]')
print(f"print(len(basket)) ----> 5")

print(f'\n# .append()')
print(f"  new_list = basket.append(100)\n# print(new_list) ----> will return None")
print('\n## must append before assigning\n\nbasket.append(100)\nnew_list = basket\n')
print(f'  print(basket) ----> # {basket}')
print(f'  print(new_list) ----> # {new_list}\n')

insert_basket = [1,2,3,4,5,]
insert_basket.insert(5,100)
new_insert_basket = insert_basket
print(f'\n# .insert()\n')
print('  insert_basket = [1,2,3,4,5,]\n')
print(f"  new_list = insert_basket.insert(100)\n# print(new_insert_basket) ----> will return None")
print('\n## must insert before assigning\n\n  insert_basket.append(100)\n  new_insert_basket = insert_basket\n')
print(f'  print(basket) ----> # {insert_basket}')
print(f'  print(new_insert_basket) ----> # {new_insert_basket}\n')

# .extend() - takes an iterable as it's param and 'add's in place' the iterable to the end of a list

extend_basket = [1,2,3,4,5,]
extend_basket.extend([100, 101])
new_extend_basket = extend_basket
print("# .extend() - takes an iterable as it's param and 'adds in place' the iterable to the end of a list\n## no return value")
print("\nnew_extend_basket = extend_basket.insert([100, 101]) ----> will return None")
print("\n## must extend before assigning\n\nextend_basket.extend([100, 101])\nnew_extend_basket = extend_basket")
print(f'  print(basket) ----> # {extend_basket}')
print(f'  print(new_extend_basket) ----> # {new_extend_basket}\n')

# REMOVING
## .pop() - removes the object at the end of the list - RETURNS THE VALUE OF THE THING JUST "POPPED"

rem_basket = [1,2,3,4,5,100,101]
rem_basket.pop()
pop_rem_basket = rem_basket[0:]
pop_rem_basket = rem_basket
pop_rem_basket.pop(0)

print()
print("  rem_basket = [1,2,3,4,5,100,101]")
print("  rem_basket.pop() # rems the last object in a list")
print(f"  print(rem_basket) ----> {rem_basket}")
print(f"\n# can specify the index to be removed - .pop(0) will remove the object at the first index\n")
print(f"  pop_rem_basket.pop(0)")
print(f"  print(rem_basket) ----> {pop_rem_basket}\n")

# .remove() - we give it a value that we want to remove, no return value
remove_rem_basket = [1,2,3,4,5,100,101]
remove_rem_basket.remove(3)
print("# .remove() - we give it a value that we want to remove\n")
print("  remove_rem_basket = [1,2,3,4,5,100,101]")
print(f"  remove_rem_basket.remove(100)")
print(f"  print(remove_rem_basket) ----> {remove_rem_basket}")

# .clear() - clears a list, no return value, alters the list
clear_rem_basket = [1,2,3,4,5,100,101]
# could also do clear_rem_basket.clear(), without assigning to a new variable
cleared_list = clear_rem_basket.clear()
print("  clear_rem_basket = [1,2,3,4,5,100,101]")
print(f"  cleared_list = clear_rem_basket.clear()")
print(f'  print("cleared_list") ----> {cleared_list}')
print(f'  print("cleared_list") ----> {clear_rem_basket}')

# .index(value, [start, stop])

index_basket = ['a','b', 'c', 'd', 'e']

print("  index_basket = ['a','b', 'c', 'd', 'e'] ")
print(f"  print(index_basket.index('d')) ----> {index_basket.index('d')}")
print(f"  print(index_basket.index('d', 0, 3)) ----> # will error out because 'd' is at the index of  and the method is starting at 0 and stopping right before it reads 3")
print(f"  print(index_basket.index('d', 0, 4)) ----> {index_basket.index('d', 0, 4)} which is the index of 'd'in index_basket")

# KEYWORD index_basket
## 'in'is a reserved keyword

print("\n# 'in'is a reserved keyword\n")
print("  index_basket = ['a','b', 'c', 'd', 'e'] ")
print(f"  print('d' in index_basket) ----> # {'d' in index_basket}")
print(f"  print('x' in index_basket) ----> # {'x' in index_basket}")

print(f"# works on strings to\n  print('x' in 'index_basket') ----> # {'x' in 'index_basket'}")
print(f"# works on strings to\n  print('q' in 'index_basket') ----> # {'q' in 'index_basket'}")

# .count(value) - returns the number of occurrences of value
print(f"\n# .count(value) - returns the number of occurrences of value\n")
print(f"  print(index_basket.count('b')) ----> # {index_basket.count('b')}")
print(f"  print('index_basket as a string'.count('s')) ----> # {'index_basket as a string'.count('s')}")
print(f"  print('index_basket as a string'.count('z')) ----> # {'index_basket as a string'.count('z')}")

# .sort() - no return value, modifies in place
sort_basket = ['a','b', 'c', 'd', 'e', 'd', 'a']
sort_basket.sort()
print("\n# .sort() - no return value, modifies\n")
print("  sort_basket = ['a','b', 'c', 'd', 'e', 'd', 'a']")
print("  sort_basket.sort()")
print(f"  print(sort_basket) ----> # {sort_basket}")

# BUILT IN FUNCTION:  sorted(list_to_sort) produces a new list (does not modify the original list)
sorted_method_basket = ['a','b', 'c', 'd', 'e', 'd', 'a']
sorted(sorted_method_basket)
print('\n# METHOD sorted(list_to_sort)\n')
print("  sorted_method_basket = ['a','b', 'c', 'd', 'e', 'd', 'a']")
print('  sorted(sorted_method_basket)')
print(f"  print(sorted_method_basket) ----> # {sorted(sorted_method_basket)}")

# .copy() copies a list and returns a new list

copy_sorted_method_basket = sorted_method_basket.copy()
print("\n# copy_sorted_method_basket = sorted_method_basket.copy()\n")
print("  copy_sorted_method_basket = sorted_method_basket.copy()")
print(f"  print(copy_sorted_method_basket) ----> # {copy_sorted_method_basket}")

# .reverse() - no return value, acts in place
reversed_basket = [1, 2, 3, 4, 5]
reversed_basket.reverse()
print("\n# .reverse() - no return value, acts in place (does not sort)\n")
print("  reversed_basket = [1, 2, 3, 4, 5]")
print(f"  print(reversed_basket) ----> # {reversed_basket}")

# reverse with slicing - creates a new copy of the list
slice_reverse_basket = [1, 2, 3, 4, 5]
print('\n# another way to reverse a list is to use slicing\n')
print("  slice_reverse_basket = [1, 2, 3, 4, 5]")
print(f"  print(slice_reverse_basket[::-1]) ----> # {slice_reverse_basket[::-1]}")

# range(start, stop)
list(range(1,100))
list(range(100))
print("list(# range(start, stop))")
print(f"list(range(1,100)) ----> # {list(range(1,100))} (note that it stops at 99)")
print(f"list(range(100)) ----> # {list(range(100))} (note that it stops at 99)")

# .join()
## takes an iterable as a param
## has a return value

sentence = "!!"
new_sentence = sentence.join(['hi', 'my', 'name', 'is', 'SLIM SHADY'])
add_spaces = ' '.join(['hi', 'my', 'name', 'is', 'SLIM SHADY'])

print(f"\n# .join()\n## takes an iterable as a param\n## has a return value\n")
print('  sentence = "!!"')
print("  new_sentence = sentence.join(['hi', 'my', 'name', 'is', 'SLIM SHADY'])")
print("  add_spaces = ' '.join(['hi', 'my', 'name', 'is', 'SLIM SHADY'])")
print(f"  print(new_sentence) ----> # {new_sentence}")
print(f"  print(add_spaces) ----> # {add_spaces}")

# list unpacking 
# a,b,c = [1,2,3]
# print("\n# list unpacking\n")
# print("  a,b,c = [1,2,3]")
# print(f"  print(a) ----> # {a}")
# print(f"  print(b) ----> # {b}")
# print(f"  print(c) ----> # {c}")


e,f,g, *new_variable_name, h = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh']
print("  a,b,c = [1,2,3]")
print(f"  print(e) ----> # {e}")
print(f"  print(f) ----> # {f}")
print(f"  print(g) ----> # {g}")
print(f"  print(h) ----> # {h}")
print(f"  print(new_variable_name) ----> # {new_variable_name}")

# None - special data type (similar to null)
none_val = None
print("\n# None - special data type (similar to null)\n")
print("  none_val = None")
print(f"  print(none_val) ----> # {none_val}")


print('\n############################################################################################\n')
