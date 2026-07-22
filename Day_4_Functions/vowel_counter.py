"""
Algorithm: Reusable Vowel Counter
Description: Wraps a vowel-counting loop inside a function with a local accumulator, returning the final count.
Author: Aryan
"""

def count_vowels(words):
    count = 0
    for i in words.lower():
        if i in "aeiou":
            count = count + 1
    return count 

# test_a = count_vowels("aryan")
# print(test_a)
