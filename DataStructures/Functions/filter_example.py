# filter() function
# syntax: filter(func, iterable) --> return value is iterator
# checks if the return value is Truthy or false
# If false, it filters out the return value from the iterator
list_1 = [0, 1, 2, 3, 4, 5]


def is_even(x):
    return x % 2 == 0


def func1(x):
    return x


print("When return value is not none:", list(filter(is_even, list_1)))
print("When return value is none:", list(filter(func1, list_1)))
'''
When return value is not none: [0, 2, 4]
When return value is none: [1, 2, 3, 4, 5]
'''

## Why is 0 omitted in the second filter() run
## because 0 is Falsy - so it gets filtered out 
## Other iterable values are non-falsy, so they are displayed
## remember, filter() function only takes one iterable (list, string, tuple, dict)

