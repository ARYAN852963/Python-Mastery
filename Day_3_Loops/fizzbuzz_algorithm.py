"""
Algorithm: FizzBuzz
Description: Solves the classic FAANG interview question using the correct order of operations for multiple conditionals.
Author: Aryan
"""

for i in range(1, 51):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
