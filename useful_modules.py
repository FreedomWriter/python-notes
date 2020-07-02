# COLLECTION MODULE

from collections import Counter, defaultdict, OrderedDict
import datetime
from array import array

li = [1,2,3,4,5,6,7]

# Counter creates a dictionary (hashmap) with the key being an item in an iterable and the value being the number of cocurances. Helps with optimziation problems
print(Counter(li))

# defaultdict allows you to provide a default value to keys that don't exist in the dictionary, allowing you to call keys that don't exist and provide them a default value.
## this built in function requires a callable object as it's first param:
### defaultdict(callable, {'key': value})
dictionary = defaultdict(lambda: 'default value',{'a': 1, 'b':2})
dictionary2 = defaultdict(lambda: 'default value',{'a': 1, 'b':2})

dictionary3 = defaultdict(lambda: 'no initial dict')
# print(dictionary['c'])
print(dictionary3['first'])

# OrderedDict()

d = OrderedDict()
d['a'] = 1
d['b'] = 2

d2 = OrderedDict()
d2['a'] = 1
d2['b'] = 2

# There are some perfomance implicaitons in chosing to use an OrderedDict
# changing the order of insertion would cause d2 != d
# note 'b' beinging inserted before 'a' in d2
    # d = OrderedDict()
    # d['a'] = 1
    # d['b'] = 2

    # d2 = OrderedDict()
    # d2['b'] = 2
    # d2['a'] = 1
print(d2 == d)
# this would return true as long as the key/value pairs were equal, standard dicts do not care about order of insertion
print(dictionary2 == dictionary)

################################################################################################
# SCRATCH ALL OF THE ABOVE ABOUT ORDERED DICTS, VERION 3.7 MADE DICTIONARIES ORDERED BY DEFAULT
################################################################################################

print(datetime.time(5,45,2))
print(datetime.date.today())

# lists in python are dynamic
# python arrays take up less memory and perform faster
# arrays can be used to make large lists more performant

# syntax: array(typecodde, data)
# 'i' is for signed integer
arr = array('i', [1,2,3])

print(arr)
print(arr[0])