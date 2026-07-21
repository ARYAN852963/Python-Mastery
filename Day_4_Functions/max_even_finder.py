"""
Algorithm: Max Even Finder
Description: The ultimate Day 4 boss challenge. Merges King of the Hill and Modulo algorithms to extract the maximum even value from an array.
Author: Aryan
"""

def get_max_even(num_list):
    count = 0 # The Small king or the weak one.
    for i in num_list:
        if i % 2 == 0 and i > count:
            count = i
    return count

# test_list = [13, 22, 9, 45, 102, 73, 10]
# test_a = get_max_even(test_list)
# print(test_a)
