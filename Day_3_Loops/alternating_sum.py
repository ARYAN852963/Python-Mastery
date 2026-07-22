"""
Algorithm: Alternating Sum (The Toggle Trap)
Description: Iterates over a range of numbers, subtracting evens and adding odds to an accumulator.
Author: Aryan
"""

box = 0

for i in range(1, 11):
    if i % 2 == 0:
        box = box - i
    else:
        box = box + i

print(box)
