"""
Algorithm: Multiplication Table Generator
Description: Dynamically generates a 1-10 multiplication table for any user-provided integer.
Author: Aryan
"""

numbers = int(input("Enter your number: "))

for num in range(1, 11):
    print(f"{numbers} x {num} = {numbers * num}")
