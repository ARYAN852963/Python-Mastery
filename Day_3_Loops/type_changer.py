"""
Algorithm: The Type Changer
Description: Converts an integer to a string to iterate and reverse it, then converts back to an integer to perform math.
Author: Aryan
"""

numbers = int(input("Enter a number: "))
number_str = str(numbers)

box = ""

for i in number_str:
    box = i + box

box = int(box)
box = box * 2
print(box)
