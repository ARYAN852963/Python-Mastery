"""
Algorithm: Password Validator
Description: Uses the len() function internally to validate string length and return Boolean values.
Author: Aryan
"""

def is_valid_password(password):
    if len(password) >= 8:
        return True
    else:
        return False

# test_a = is_valid_password("Ayan")
# print(test_a)
