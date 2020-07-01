# METHOD RESOLUTION ORDER - MRO
# # MRO does a depth first search - watch for tricky instances http://www.srikanthtechnologies.com/blog/python/mro.aspx
# visual for how the below classes relate to each other
#     A
#   /  \
#  /    \
# B      C
# \      /
#  \    /
#    D 



class A():
    num = 10

class B(A):
    pass

class C(A):
    num = 1

class D(B,C):
    pass

print(D.mro())
