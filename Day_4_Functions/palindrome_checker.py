"""
Algorithm: Palindrome Checker
Description: A FAANG-level algorithm that reverses a string internally and evaluates if it matches the original string.
Author: Aryan
"""

def s_palindrome(word):
    reversed_word = ""
    for i in word:
        reversed_word = i + reversed_word
    if reversed_word == word:
        return True
    elif reversed_word != word:
        return False

# test_a = s_palindrome("madam")
# print(test_a)
