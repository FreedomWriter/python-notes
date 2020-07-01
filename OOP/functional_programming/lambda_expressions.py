# lambda expressions
## ONE TIME anonymous functions

# SYNTAX
## lambda paramater: manipulation(param)

from functools import reduce

my_list = [1,2,3,4,5]
your_list = ['one', 'two', 'three', 'four', 'five']



print(list(map(lambda item: item*2, my_list)))

print(list(filter(lambda item: item > 2, my_list)))

print(reduce(lambda acc, item:  acc+item, my_list))