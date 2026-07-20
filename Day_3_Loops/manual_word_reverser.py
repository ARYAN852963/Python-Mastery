"""
Algorithm: Manual Word Reverser
Description: Reverses a string character-by-character using a string accumulator without relying on built-in functions.
Author: Aryan
"""

word = input("Enter your word: ")
new_word = ""

for letter in word:
    new_word = letter + new_word

print(new_word)
