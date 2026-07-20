"""
Algorithm: FizzBuzz
Description: Solves the classic FAANG interview question using the correct order of operations for multiple conditionals.
Author: Aryan
"""

for i in range(1, 31):
    if i % 2 == 0 and i % 3 == 0:
        print("FuzzBizz")
    elif i % 2 == 0:
        print("Fuzz")
    elif i % 3 == 0:
        print("Bizz")
    else:
        print(i)
