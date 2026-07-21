"""
Algorithm: The Prime Factory
Description: Evaluates primality by executing modulo math within a for/else loop architecture.
Author: Aryan
"""

def is_prime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    else:
        return True

# test_a = is_prime(10)
# print(test_a)
