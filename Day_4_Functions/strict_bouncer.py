"""
Algorithm: Strict Bouncer Logic
Description: Validates age and VIP status using a function with conditional branching (if/elif).
Author: Aryan
"""

def check_id(age, has_vip_pass):
    if age >= 18:
        return "Welcome in!"
    elif age < 18 and has_vip_pass == True:
        return "Welcome in, VIP!"
    elif age < 18 and has_vip_pass == False:
        return "Nikal Gyo gareeb"

# test_a = check_id(19, True)
# print(test_a)
