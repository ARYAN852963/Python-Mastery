"""
Algorithm: Weather Converter
Description: Performs complex math operations on integer arguments dynamically based on string inputs.
Author: Aryan
"""

def covert_temp(temp, Scale):
    if Scale in "C":
        return (temp * 9/5) + 32
    if Scale in "F":
        return (temp - 32) * 5/9

# test_a = covert_temp(100, "F")
# print(test_a)
