# Day 10: Bulletproofing Your Code
*Error Handling, Advanced Arguments & Edge Cases*

**Time Limit: 60 Minutes.**
You are strictly forbidden from asking for hints until the timer expires. You must use `python filename.py` to test your own code.

---

## Level 1: The Try / Except Shield (Fundamentals)
*Build the armor. Do not let the program crash.*

**Question 1:** Build a script that asks a user to input their birth year. Convert it to an integer. If they type a word instead of a number, catch the specific exception and display a custom error message. 
**Question 2:** Create a list of 3 cities. Ask the user for an index number to print a city. Catch the specific error that happens if they type `5` (an index that doesn't exist) and print `"City not found."`
**Question 3:** Write a division function `safe_divide(x, y)`. It must handle both division by zero AND the scenario where the user passes a string instead of a number. (You will need multiple `except` blocks).
**Question 4:** Create a function `read_file(filename)`. Attempt to open and read a file that doesn't exist (e.g., `ghost.txt`). Catch the error and print a warning. Include a `finally` block that prints `"File read attempt finished."` regardless of success or failure.

---

## Level 2: Raising Alarms & Infinite Arguments (Logic Builder)

**Question 5:** Write a function `process_payment(amount)`. If the amount is negative, manually trigger a `ValueError` with a custom message. Test the crash.
**Question 6:** Write a function `sum_all()` that accepts an infinite amount of positional arguments. It must return the total sum of all arguments passed. Test it with 5 arguments.
**Question 7:** Write a function `display_team(**kwargs)`. It should accept an infinite amount of keyword arguments (e.g., `manager="Alice", developer="Bob"`). Print each key and value dynamically.
**Question 8:** Write a function `create_server_config(ip_address, *args, **kwargs)`. It requires an IP address, accepts any number of optional port numbers as `*args`, and accepts any number of setting overrides (like `timeout=30`, `debug=True`) as `**kwargs`. Return all three components as a formatted string. 

---

## Level 3: The Boss Level (Combined Architecture)

**Question 9:** Build an `Authenticator` class. It should have a private list `__banned_users`. Create a method `login(username)`. If the username is in the banned list, manually raise a `PermissionError`. If the username is empty, raise a `ValueError`. Otherwise, return `"Login successful"`. 
**Question 10 (BOSS):** Create a function `bulk_register(*args)`. This function takes an infinite number of usernames. Inside the function, loop through the usernames and attempt to pass each one to your `Authenticator.login()` method. Wrap the login attempt in a `try/except` block. If a user triggers a `PermissionError` or `ValueError`, catch it, print the exact error message, and *continue* the loop for the rest of the users without crashing the script.

---

**Execution:** Create a file named `bulletproof.py` in your `Day_10_Bulletproofing` folder and solve all 10 questions. Start the timer.
