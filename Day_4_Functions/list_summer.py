"""
Algorithm: The List Summer
Description: Accepts a list as an argument, iterates through its elements, and sums them using a local accumulator.
Author: Aryan
"""

def sum_list(numbers):
    total = 0
    for i in numbers:
        total = i + total
    return total

# test_list = [10, 20, 30, 40, 50]
# test_a = sum_list(test_list)
# print(test_a)
