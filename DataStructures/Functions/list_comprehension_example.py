## List Comprehensions
## Syntax: [expression 1 for iteration if expression 2]

def square(x):
    return x ** 2


result = map(square, range(11))
print("Result using map() function {}".format(list(result)))

result_list_comp=[x**2 for x in range(11)]
print("result with list Comprehension with only expression 1: {}".format(list(result_list_comp)))

result_list_comp=[x**2 for x in range(11) if x%2 == 0]
print("result with list Comprehension and expression 2: {}".format(list(result_list_comp)))
# print(result == result_list_comp) ## Objects are different, first is an iterator object, second is a list class object, so this should be False
# print(list(result) == result_list_comp) ## this should be True as we are comparing values here
