#Upper Bound: O(n^2*n) time | O(n*n!) space

def get_permutations(arr):
    permutations = []
    # the empty list is holding the place for whatever permutation we are currently constructing
    permutations_helper(arr, [], permutations)
    return permutations

def permutations_helper(arr, cur_perm, permutations):
    # check if we have numbers left in the array AND that the cur_perm has things in it - we never want to append the default empty array
    if not len(arr) and len(cur_perm):
        permutations.append(cur_perm)
    else:
        for i in range(len(arr)):
            # remove the number from array and generate a new array
            new_arr = arr[:i] + arr[i +1:]
            # create a new permutation snapshot consting of cur_per + el at arr[i]
            new_permutation = cur_perm + [arr[i]]
            permutations_helper(new_arr, new_permutation, permutations)

# Upper

def get_perms(arr):
    permutations = []
    perm_helper(0, arr, permutations)
    return permutations

def perm_helper(i, arr, permutations):
    # are we at the end of our array?
    if i == len(arr) -1:
        permutations.append(arr[:])
    else:
        # we want to iterate through the nums starting at our curr position and swap all of the next numbers with our curr position
        for j in range(i, len(arr)):
            # first run is j == i which is intentional
            # next pass j == i + 1
            # next pass will be j == i + 2
            # [1,3, ...]
            swap(arr, i, j)
            # [2, 1, ... ]
            perm_helper(i + 1, arr, permutations)
            swap(arr, i, j)
            # [1, 2, ...]

def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]


print(get_perms([1,2,3,4]))
print(get_permutations([1,2,3,4]))