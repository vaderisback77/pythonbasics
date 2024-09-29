### syntax
### lambda [parameters list]: expression
### Lambdas are anonymous functions 
### they don't have names so that's why they are called anonymous
### Lambdas return a function object which can be returned to a variable


square = lambda x : x**2
## this is equivalent to

def square_func(x):
    return x**2

print(type(square)) # should return a function object
print(type(square_func))
print(square(2))
print(square(3))

""" 
Output:
<class 'function'>
<class 'function'>
4
9
"""
from math import sqrt
square_root = lambda x: sqrt(x)
print(square_root(100))


## lambda functions can be passed as paramters to a regular function
## but lambdas are single expression functions, so you cannot do assignments like x = 5 for example


def calculate_square_root(x, fn):
    return fn(x)

def calculate_square(y, fn):
    return fn(y)

g = calculate_square_root(3, square_root)
h = calculate_square(3, square)
print("square root: {} and square: {}".format(g, h)) 


