"""
Algorithm: King of the Hill (Max Value)
Description: Iterates through an array to find and isolate the maximum value.
Author: Aryan
"""

scores = [45, 22, 89, 12, 104, 3, 99]
max_score = 0

for giant in scores:
    if giant > max_score:
        max_score = giant
        
print(max_score)
