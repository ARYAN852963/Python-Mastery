"""
Algorithm: Fibonacci Sequence Generator
Description: Generates the first 15 numbers of the Fibonacci sequence using variable swapping logic.
Author: Aryan
"""

a = 0
b = 1 

for i in range(15):
    print(a)
    next_number = a + b
    a = b
    b = next_number
