import random
import time

my_range = 500000
my_size = 10000

random_nums = random.sample(range(my_range), my_size)
# random_nums = [4, 10, 13, 17, 21, 26, 29, 31, 32, 50, 67, 60, 74, 85, 92]

print(random_nums)
num_to_find = 4578

# O(N) - linear time
def linear_search(arr, target):
    for num in arr:
        if num == target:
            return True
        
    return False

# print(linear_search(random_nums, num_to_find))

print('Linear')
start = time.time()
print(linear_search(random_nums, num_to_find))
end = time.time()
print(f"Runtime: {end - start}")

random_nums.sort()
# print(random_nums)

def binary_search(arr, target):
    start = 0
    end = (len(arr) -1)

    found = False
    while end >= start and not found:
        
        # find middle index of array
        middle_index = (start + end) //2
        # compare the value in the middle with target# if the middle value is the same as target, set found to True
        if arr[middle_index] == target:
            found = True
        # move start or end index closer to one another, and shrink our search space
        else:
            if target < arr[middle_index]:
                end = (middle_index -1) 
            if target > arr[middle_index]:
                start = (middle_index + 1)
    return found
    
print('Binary')
start = time.time()
print(binary_search(random_nums, num_to_find))
end = time.time()
print(f"Runtime: {end - start}")