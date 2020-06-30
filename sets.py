# SETS
## UNORDERED collections of unique objects
### adding duplicate values to a set will not break, but the duplicate item will not actually get added
### means no indexing
## can use 'in' keyword to find a value in a set
## can use built in method len(set) to find the length of a set
## can convert a set to a list
## can use .copy()

my_set = {1,2,3,4,5,5}

print("\n  my_set = {1,2,3,4,5,5}\n")
print("    print(my_set) ----> # {1,2,3,4,5}")
print("\n  my_set.add(100)\n  my_set.add(2)\n\n    print(my_set) ----> # {1,2,3,4,5,100} - UNIQUE values only\n     # the second 5 is never initialized\n     # the duplicate add of 2 does not get added (no error returned)\n    print(len(my_set)) ----> # 5")

# remove duplicates from a list using set
print("\n# remove duplicates from a list using set\n\n  my_list = [1,1,2,2,3,3,4,5]\n  no_dupes = set(my_list)\n\n   print(my_list) ----> # [1,1,2,2,3,3,4,5]\n   print(no_dupes) ----> # {1, 2, 3, 4, 5}")

my_list = list(my_set)
# print(my_list)

print("\n# convert a set to a list\n")
print(f"  my_list = list(my_set)\n    print(my_list) ----> # {my_list}")

for i,char in enumerate(list(range(100))):
  if char == 50:
    print(f"index of 50 is: {i}")

print('\n############################################################################################\n')