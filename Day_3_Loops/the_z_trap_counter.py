"""
Algorithm: The Z-Trap Vowel Counter
Description: Counts vowels in a string but instantly terminates the loop using `break` if the letter 'z' is encountered.
Author: Aryan
"""

sentence = input("Enter a sentence: ")
count = 0

for i in sentence.lower():
    if i in "aeiou":
        count = count + 1
    elif i == "z":
        print("Trap")
        break
        
print(count)
