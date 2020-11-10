# def rotateImage(a):
#     # print("a", a)
#     print("NEW NEW NEW NEW NEW NEW NEW NEW")
#     n = len(a[0])   
#     print("n", n)     
#     # transpose matrix
#     for i in range(n):
#         print("******************************")
#         print("i", i)
#         for j in range(i, n):
#             print(f"a[i: {i}][j: {j}]", "Original Value", a[i][j], " | ",   f"a[j: {j}][i: {i}]", "New Value", a[j][i])
#             print("---------------")
#             print("a", a)
#             print("---------------")
#             a[j][i], a[i][j] = a[i][j], a[j][i] 
#             print("---------------")
#             print("a", a)
#             print("---------------")
    
#     # reverse each row
#     for i in range(n):
#         a[i].reverse()
        
#     print(a)
#     return a

# rotateImage([[5 ,10 ,15 ,20], [25 ,30, 35, 40], [45, 50, 55, 60], [65, 70, 75, 80]])


def rotateImage(a):
    # print("a", a)
    print("NEW NEW NEW NEW NEW NEW NEW NEW")
    n = len(a[0])       
    # transpose matrix
    for i in range(n):
        for j in range(i, n):
            a[j][i], a[i][j] = a[i][j], a[j][i] 
    
    # reverse each row
    for i in range(n):
        a[i].reverse()
        
    print(a)
    return a

rotateImage([[5 ,10 ,15 ,20], [25 ,30, 35, 40], [45, 50, 55, 60], [65, 70, 75, 80]])

'''
Turn this:

[
    [5 ,10 ,15 ,20],
    [25 ,30, 35, 40],
    [45, 50, 55, 60],
    [65, 70, 75, 80]
] 

Into this:

[
    [65, 45, 25, 5],
    [70, 50, 30, 10],
    [75, 55, 35, 15],
    [80, 60, 40, 20]
]

In this example we are working with a square matrix.

Define n as the length of one array in the matrix.
 - this doesn't accomplish anything other then saving us keystrokes, 
    instead of typing `len(a[0]` in both for loops, we can subsitute `n`)


enter the i for loop, which loops over the range(n):

    FIRST ITERATION OF `I` LOOP
    i = 0
    J LOOP WILL ITERATE COMPLETELY, FROM I - N AT WHICH POINT WE WILL RE-ENTER THE `I` LOOP
    enter the j for loop, which also loops over the range(n):
        j = 0
        a[0], a[0] = a[0], a[0] --> 5 stayed in the same position
        j = 1
        a[1], a[0] = a[0], a[1] --> 25 moved to where 10 was, and vice versa
        j = 2
        a[2], a[0] = a[0], a[2] --> 45 moved to where 15 was, and vice versa
        j = 3
        a[3], a[0] = a[0], a[3] --> 65 moved to where 20 was, and vice versa

        # We are now done with this iteration of the inner loop (j), our matrix looks like this
        # as we move into the second iteration of the outer loop:

        [
            [5 ,25 ,45 , 65], # This row is now sorted, and it's old values have been swapped in place
            [10 ,30, 35, 40],
            [15, 50, 55, 60],
            [20, 70, 75, 80]
        ]

    SECOND ITERATION OF `I` LOOP

    i = 1

    enter the j for loop, which also loops over the range(n):
        j = 1
        a[1], a[1] = a[1], a[1] --> 30 stayed in the same position
        j = 2
        a[2], a[1] = a[1], a[2] --> 50 moved to where 35 was, and vice versa
        j = 3
        a[3], a[1] = a[1], a[3] --> 70 moved to where 40 was, and vice versa

        # We are now done with this iteration of the inner loop (j), our matrix looks like this
        # as we move into the second iteration of the outer loop:

        [
            [5 ,25 ,45 , 65],
            [10 ,30, 50, 70], # This row is now sorted, and it's old values have been swapped in place
            [15, 35, 55, 60],
            [20, 40, 75, 80]
        ]

    Third ITERATION OF `I` LOOP

    i = 2

    enter the j for loop, which also loops over the range(n):
        j = 2
        a[2], a[2] = a[2], a[2] --> 55 stayed in the same position
        j = 3
        a[3], a[2] = a[2], a[3] --> 75 moved to where 60 was, and vice versa

        # We are now done with this iteration of the inner loop (j), our matrix looks like this
        # as we move into the second iteration of the outer loop:

        [
            [5 ,25 ,45 , 65],
            [10 ,30, 50, 70],
            [15, 35, 55, 75], # This row is now sorted, and it's old values have been swapped in place
            [20, 40, 60, 80]
        ]

    Fourth ITERATION OF `I` LOOP

    i = 3

    enter the j for loop, which also loops over the range(n):
        j = 3
        a[3], a[3] = a[3], a[3] --> 80 stayed in the same position
        
        We exit the `j` loop, since the next value for j would be 4, which is outside of our range
        

        [
            [5 ,25 ,45 , 65],
            [10 ,30, 50, 70],
            [15, 35, 55, 75],
            [20, 40, 60, 80]
        ]

    The only thing left to do is sort the nested arrays so that the values appear in the proper order!

    We can do this by looping over a and reversing each array

    for i in range(n):
        a[i].reverse()
'''