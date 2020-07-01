# DUNDER AKA MAGIC METHODS

class Toy():
    def __init__(self, color, age):
        self.color = color
        self.age = age
        self.my_dict = {
            'name': 'yoyo',
            'has_pets': False
        }

    def __str__(self):
        return f'{self.color}'

    def __len__(self):
        return 5
    ## makes a class `callable`: print(action_figure()) note the invocation, this isn't possible without __call__
    def __call__(self):
       return('yes?')

    ## allows action_figure to access my_dict through bracket notation
    def __getitem__(self, i):
        return self.my_dict[i]

action_figure = Toy('red', 0)

# the dunder method and built in function were modified for action_figure ONLY
print(action_figure.__str__())
print(str(action_figure))

print(action_figure.__len__())
print(len(action_figure))

print(action_figure())
print(action_figure['name'])
print(action_figure['has_pets'])

# some_num = 678
# print(type(some_num.__str__()))
# print(type(str(some_num)))

# print(len(some_num.__str__()))
# print(len(str(some_num)))