# Some functions available
# # map(callback, data)
# # filter(callback, data)
# # zip(callback, data)
# # reduce(callback, data) - reduce needs to be imported from functools
# # # `from functools import reduce`

from functools import reduce

my_list = [1,2,3,4,5]
your_list = ['one', 'two', 'three', 'four', 'five']

# MAP
## does map things
## needs to be wrapped in the list functions

def map_func(item):
    return item * 2

# print(list(map(map_func, my_list)))
# print(my_list)

# FILTER
## filters items based on conditional
## needs to be wrapped in the list functions

def filter_func(item):
    return item > 3

print(list(filter(filter_func, my_list)))
print(my_list)

# REDUCE
## reduces just like js, does not need to be wrapped in list()
def reduce_func(acc, item):
    return acc + item

print(reduce(my_list, your_list))
print(my_list)

# zip
## returns a tuple with the two iterables `zipped` together
## needs to be wrapped in the list functions

print(list(zip(my_list, your_list)))
print(my_list)