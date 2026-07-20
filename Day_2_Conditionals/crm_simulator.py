"""
Algorithm: CRM Login Simulator
Description: Validates a user's login credentials against a simulated database and provides specific error routing using if/elif/else conditions.
Author: Aryan
"""

db_username = "admin"
db_password = "password123"

username = input("Enter your username: ")
password = input("Enter your password: ")

if username == db_username and password == db_password:
    print("Login Successful")
elif username == db_username:
    print("Incorrect Password")
else:
    print("User not found")
