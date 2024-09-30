# map() function
# Syntax: map(func, *iterables) ---> return value is iterator
# returns an iterator that calculates the function applied to each element of the iterables
# iterables is multiple lists, tuples, strings (anything where an element can be called by its index)

# equal length iterables
list_1 = [1, 2, 3]
list_2 = [4, 5, 6]


def multiply(x, y):
    return x * y


def square(x):
    return x**2


result = map(multiply, list_1, list_2)
print(result, type(result))
print(list(result))


# Unequal length iterables
list_1 = [1, 2, 3, 7, 8, 9]
list_2 = [4, 5, 6, 11, 13, 15, 17]
result = map(multiply, list_1, list_2)
print(result, type(result))
print(list(result))

# I can also pass a single iterable like a list and do something to each element of that list like a lambda
# so it can be a single iterable as well
list_3 = [7, 8, 9]
result_2 = map(square, list_3)
print(list(result_2))



