"""
Algorithm: Weather Converter
Description: Performs complex math operations on integer arguments dynamically based on string inputs.
Author: Aryan
"""

def convert_temp(temp, scale):
    if scale == "C":
        return (temp * 9/5) + 32
    elif scale == "F":
        return (temp - 32) * 5/9

# test_a = convert_temp(100, "F")
# print(test_a)
