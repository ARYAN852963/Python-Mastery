"""
Algorithm: Perfect Number Checker
Description: Checks if a user-provided integer is a "Perfect Number" (a number that equals the sum of its proper divisors).
Author: Aryan
"""

num = int(input("Enter the number: "))
divisors = 0

for i in range(1, num):
    if num % i == 0:
        divisors = divisors + i

if divisors == num:
    print("Perfect")
else:
    print("Not-Perfect")
