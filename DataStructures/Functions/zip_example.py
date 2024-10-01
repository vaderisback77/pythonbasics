## zip() function zips and creates a tuple of the elements of an iterable
## Like map() function, it can take multiple iterables
## Syntax: zip(*iterables) --> returns an iterator

# defined 3 iterables
list_1 = [0, 1, 2, 3]
list_2 = [4, 5, 6, 7]
list_3 = [8, 9, 10, 11]

# calling zip() function 
result = zip(list_1, list_2, list_3)   # return is an iterator value
print(list(result))

'''
Output:
[(0, 4, 8), (1, 5, 9), (2, 6, 10), (3, 7, 11)]
'''

list_1 = [0, 1, 2, 3]
list_2 = [4, 5, 6, 7, 100]
list_3 = [8, 9, 10, 11, 20, 25, 30]
string_1 = "Python"  # String is also a kind of iterable

result = zip(list_1, list_3, string_1, list_2)
print(list(result))

'''
Output:
[(0, 8, 'P', 4), (1, 9, 'y', 5), (2, 10, 't', 6), (3, 11, 'h', 7)]
'''

print(tuple(zip(list_2)))