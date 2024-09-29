## Randomize a list or iterable using random() function
from random import random

## first way to randomizing a list
l = [20, 18, 90, 67, 7, 56, 49, 32]
ans = sorted(l, key=lambda list: random())
print(ans)

s = ["a", "g", "b", "d", "m"]
s_ans = sorted(s, key=lambda list: random())
print(s_ans)

## Second way of randomizing a list

name_of_attendees = ["Saurabh", "Patrick", "Mike", "Matt", "Jack"]
new_ans = sorted(name_of_attendees, key= lambda x: random())
print(new_ans)