"""
Algorithm: Vowel Encryptor
Description: Replaces all vowels in a user's string with an asterisk (*) using the `continue` keyword.
Author: Aryan
"""

message = input("Enter your secret message: ")
encrypted = ""

for i in message.lower():
    if i in "aeiou":
        encrypted = encrypted + "*"
        continue
    else:
        encrypted = encrypted + i 

print(encrypted)
