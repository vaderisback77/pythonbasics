from functools import reduce
l = [5, 2, 3, 17, 1, 29, 3]
result = reduce(lambda a, b: a if a > b else b, l)
print(result)


result = reduce(lambda x, y: x + " " + y, ("python", "is", "awesome"))  ## passing a tuple to the reduce function
print(result)

'''
Output
29
python is awesome
'''