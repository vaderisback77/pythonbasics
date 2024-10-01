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

## this program checks for the any or all truthy condition
## In ANY condition, if any element in the iterable is truthy, the result is True
## In ALL condition, ONLY if all the elements in the iterable are truthy, the result will be false
l = [0, "", None, 100]
result = reduce(lambda x, y: bool(x) or bool(y), l)
result_2 = reduce(lambda x, y: bool(x) and bool(y), l)
print(result, result_2)



