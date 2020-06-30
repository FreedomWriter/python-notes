# TUPLE
## like lists, but immutable
## cannot be sorted, reversed or any of the other methods we saw with list
## can access a particlar item in the tuple using index
## can use 'in' to determine if a value is in the tuple
## can be sliced - QUIRK - a tuple that only has a single item tends to include the trailing comma
## BENEFITS
### data is protected - lattitude and longitude would be a good use case
### more performant

print("# TUPLE\n## like lists, but immutable\n## cannot be sorted, reversed or any of the other methods we saw with list\n## can access a particlar item in the tuple using index\n## can use 'in' to determine if a value is in the tuple\n## can be sliced - QUIRK - a tuple that only has a single item tends to include the trailing comma\n## BENEFITS\n### data is protected - lattitude and longitude would be a good use case\n### more performant\n")

my_tuple = (1,2,3,4,5)
dict_tupple_key = {
  (1,2): "value for tuple key",
  'basket': [1,2,3],
  'greet': 'hello'
}
print("  my_tuple = (1,2,3,4,5)")
print("  my_tuple[1] = 'z' ----> # will error out, tuples do not support item assignment (immutable) ")
print(f"\n# a tuple can be used as a valid key in a dictionary")
print("\n  dict_tupple_key = {\n  (1,2): 'value for tuple key',\n  'basket': [1,2,3],\n  'greet': 'hello'\n  }\n")
print(f"print(dict_tupple_key[(1,2)]) ----> # {dict_tupple_key[(1,2)]}")
print(f"\n# - QUIRK ALERT - #\n  print(my_tuple[0:1]) ----> # {my_tuple[0:1]}")

print("\n# can assign to a new value\n")
one = my_tuple[0]
two = my_tuple[1]
print("  one = my_tuple[0]\n  two = my_tuple[1]\n")
print(f"    print(one) ----> # {one}")
print(f"    print(two) ----> # {two}")
first,second, *rest = (1,2,3,4,5,6,7,8,9)
print("\n  first,second, *rest = (1,2,3,4,5,6,7,8,9)\n")
print(f"    print(first) ----> # {first}")
print(f"    print(second) ----> # {second}")
print(f"    print(rest) ----> # {rest}")
print(f"    print(rest[2:5]) ----> # {rest[2:5]}")

# tuple methods
## only two
## .count() - takes a value and counts the number of instances
## .index() - takes a value and returns the index of the first occurance

print("\n# tuple methods\n## only two\n## .count() - takes a value and counts the number of instances\n## .index() - takes a value and returns the index of the first occurence\n")

# Built in functions
## len(tuple) - returns the length of the tuple

print("\n# Built in functions\n## len(tuple) - returns the length of the tuple\n")

print('\n############################################################################################\n')