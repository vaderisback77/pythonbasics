def add_numbers(nums: int) -> int: 
    total = 0
    for i in range(nums):
        total+= i
    return total

x = add_numbers(100)
y = add_numbers(1000)
print(f"Value x: {x}")
print("Value y: {}".format(y))
