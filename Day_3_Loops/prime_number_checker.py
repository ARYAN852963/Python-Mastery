"""
Algorithm: Prime Number Checker
Description: Evaluates if a given integer is a prime number using modulo checks and a break/else loop structure.
Author: Aryan
"""

number = int(input("Enter a number: "))

if number < 2:
    print("Not a prime")
else:
    for i in range(2, number):
        if number % i == 0:
            print("Not a prime")
            break
    else:
        print("Prime")
