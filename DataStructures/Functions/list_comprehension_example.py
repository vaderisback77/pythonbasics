def square(x):
    return x ** 2


result = map(square, range(11))
print("Result using map() function {}".format(list(result)))


result_list_comp=[x**2 for x in range(11)]
print("result with list Comprehension: {}".format(list(result_list_comp)))
# print(result == result_list_comp) ## Objects are different, first is an iterator object, second is a list class object, so this should be False
# print(list(result) == result_list_comp) ## this should be True as we are comparing values here
