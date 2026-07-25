# OOP Core Drills: Levels 3, 4, and 5

You mentioned you are confused about Methods, Return Values, and Inheritance. These drills are designed to lock these concepts into your brain so they translate perfectly to C++ later.

*Rule: Write the code to satisfy these system requirements. Do not copy-paste. Build them from scratch.*

## Level 3: Instance Methods (Action Mechanics)
*Goal: Understand how objects change their own data using methods.*

**Question 1:** Build a `Warrior` class. In the `__init__`, give him `health = 100`. Write a method called `take_damage()` that subtracts 20 from his health every time it is called. Instantiate the warrior, call the method twice, and print his final health.
**Question 2:** Build a `BankAccount` class. Give it a `balance` attribute (starting at 0). Write a `deposit(amount)` method that adds to the balance, and a `withdraw(amount)` method that subtracts from the balance.
**Question 3:** Build a `Car` class. Give it a `speed` attribute (starting at 0). Write an `accelerate(amount)` method that increases the speed, and a `brake(amount)` method that decreases the speed. Ensure the speed cannot go below 0!

---

## Level 4: Return Values vs Print 
*Concept Check: `print()` just shows text on a screen for humans. `return` gives the data back to the program so the computer can actually use it for math later.*

**Question 4:** Build a `Calculator` class. Write a method called `add(a, b)` that **returns** the sum of the two numbers. 
*Proof it works:* Save the result in a variable like this: `x = my_calc.add(10, 5)`. Then write `print(x + 10)`. If you used `print` inside the method instead of `return`, this will crash!
**Question 5:** Build a `Store` class. Write a method called `calculate_tax(price)` that **returns** 18% of the price (price * 0.18). 
**Question 6:** Build an `AgeVerifier` class. Write a method called `is_adult(age)`. It must **return** `True` if the age is 18 or older, and **return** `False` otherwise. 

---

## Level 5: Inheritance & `super()` (DNA Mechanics)
*Goal: Understand how to pass attributes from a parent to a child.*

**Question 7:** Build a base `Character` class. In its `__init__`, give it `name` and `health`. 
**Question 8:** Build a `Mage` class that inherits from `Character`. Give the `Mage` its own `__init__` that takes `name`, `health`, and `mana`. Use `super().__init__(name, health)` to pass the first two up to the parent, and then save `self.mana = mana` inside the Mage.
**Question 9:** Build an `Animal` class with a method called `make_sound()` that prints `"Some generic sound"`.
**Question 10 (Overriding):** Build a `Dog` class that inherits from `Animal`. **Override** the `make_sound()` method inside `Dog` so that it prints `"Bark!"` instead of the generic so