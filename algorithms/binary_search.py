import random
import time

my_range = 100
my_size = 15

random_nums = random.sample(range(my_range), my_size)

print(random_nums)
num_to_find = 12

# O(N) - linear time
def linear_search(arr, target):
    for num in arr:
        if num == target:
            return True
        
    return False

print(linear_search(random_nums, num_to_find))

random_nums.sort()
print(random_nums)

def binary_search(arr, target):
    # find middle index of array
    # compare the value in the middle with target
    #