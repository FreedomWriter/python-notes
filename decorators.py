# DECORATOR PATTERN
## decorators supercharge our functions
## a HOF that wraps a function and enhances it

## functions are first class citizens (can be passed around like variables)

from time import time

def my_decorator(func):
    def wrap_func(*args, **kwargs):
        print("\n**********")
        func(*args, **kwargs)
        print("**********\n")
    return wrap_func

@my_decorator
def simple_func():
    print("I'm just a simple func")

simple_func()

@my_decorator
def hello(greeting, emoji):
    print(greeting, emoji)


@my_decorator
def my_dec_hello(greeting, emoji='👋🏽'):
    print(greeting, emoji)

# without decorator - whats going on in this one???????????
my_decorator(hello)('hellloooooo!!!!!', '🔥')
# with decorator
hello('hellloooooo!!!!!', '🐍')
# *kwargs
my_dec_hello('hellloooooo!!!!!')

## PERFORMANCE DECORATOR

def performance(fn):
    def wrapper(*args, **kwargs):
        t1= time()
        result = fn(*args, ** kwargs)
        t2 = time()
        print(f"took {t2 - t1} s")
        return result
    return wrapper

@performance
def long_time():
    for i in range(1000000):
        i*5

long_time()