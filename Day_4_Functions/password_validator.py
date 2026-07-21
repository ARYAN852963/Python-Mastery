"""
Algorithm: Password Validator
Description: Uses the len() function internally to validate string length and return Boolean values.
Author: Aryan
"""

def is_valid_password(password):
    a = len(password)
    if a >= 8:
        return True
    elif a <= 8:
        return False

# test_a = is_valid_password("Ayan")
# print(test_a)
