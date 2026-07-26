# Day 9: The Data Flow & Scope Protocol
*Fixing the Core: Returns, Prints, and Variable Scopes.*

**Time Limit: 45 Minutes.** 
You are strictly forbidden from asking for hints until the timer expires. You must use `python filename.py` to test your own code.

---

## Level 1: The Print vs Return Trap
*Rule: Do NOT use `print()` inside these functions unless explicitly told to.*

**Question 1:** Write a function called `multiply(a, b)` that **returns** the product of `a` and `b`. Outside the function, capture the result in a variable called `answer` and print `answer`.
**Question 2:** Write a function called `get_welcome_message(name)` that **returns** the string `"Welcome to the system, [name]!"`. Print the result of calling this function.
**Question 3:** Write a function called `is_even(number)` that **returns** `True` if the number is even, and `False` if it is odd. 
**Question 4 (The Chain):** Use the functions from Q1 and Q3 together. Pass `multiply(4, 5)` directly into `is_even()`. Print the final boolean result. *(Hint: This only works because Q1 uses `return` instead of `print`!)*

---

## Level 2: Variable Scopes (Local vs Global)
*Rule: Understand where variables live and die.*

**Question 5:** Create a global variable `company = "OpenAI"`. Write a function `change_company()` that creates a local variable `company = "DeepMind"` and returns it. Print the global `company`, then print the result of `change_company()`. Notice how they don't overwrite each other.
**Question 6:** Create a global variable `counter = 0`. Write a function `increment()` that uses the `global` keyword to add 1 to `counter`. Call the function 3 times, then print `counter`.
**Question 7:** Write a function `calculate_total(price)` that creates a local variable `tax = 0.20`. It should **return** the `price + (price * tax)`. Try to print `tax` *outside* the function. (It should crash. Leave a `# comment` explaining why it crashes).

---

## Level 3: The Boss Level (Data Flow in Classes)
*Testing everything you know without leaking data.*

**Question 8:** Build a class `ShoppingCart`. It should have an `__init__` method that creates a private list `__items = []`. 
**Question 9:** Add a method `add_item(item_name)` that appends the item to the private list and **returns** the string `"Item Added"`. Do not `print()` inside this method.
**Question 10 (BOSS):** Add a method `get_items()` that **returns** the private list so the user can see what they bought. Outside the class, create a cart, add "Laptop" and "Mouse", and `print()` the result of `get_items()`.


**Execution:** Create a file named `data_flow.py` and solve all 10 questions. Start the timer.
