# Day 7: Inheritance and Advanced OOP

**Time Limit: 60 Minutes**
*Rule: Do not ask for help until the timer rings. Struggle builds the engineer.*

## Level 1: Syntax Sprints (Fundamentals)
*Muscle memory. Build these fast.*

**Question 1:** Create a base class called `Vehicle` that has an `__init__` method taking `brand` and `speed`. Then, create an empty subclass called `Car` that inherits from `Vehicle` using the `pass` keyword.
**Question 2:** Instantiate a `Car` object with the brand "Toyota" and speed 120. Print the object's `brand` and `speed` to the terminal to prove it inherited the attributes.
**Question 3:** Add a method called `honk()` to the `Vehicle` class that prints `"Beep!"`. Call `.honk()` using your `Car` object to prove methods are also inherited.

---

## Level 2: Logic Builders (Overriding & Super)
*Now you are manipulating the inheritance.*

**Question 4:** Create a base class `Employee` with `name` and `salary`. Create a subclass called `Manager` that inherits from `Employee`.
**Question 5:** Inside the `Manager` class, create its own `__init__` method that takes `name`, `salary`, and `department`. Use the `super().__init__(name, salary)` function to let the parent class handle the first two, and then assign `self.department = department`.
**Question 6:** Add a `work()` method to `Employee` that prints `"[Name] is working."`. Then, **override** the `work()` method inside `Manager` so that it instead prints `"[Name] is managing the [department] department."`
**Question 7 (Polymorphism):** Create a list that contains two `Employee` objects and one `Manager` object. Write a `for` loop that iterates through the list and calls `.work()` on each object. Watch how Python automatically knows which version of the method to use!

---

## Level 3: The Logic Gym (Brain Burners)
*This is where you earn your 1% status. Read carefully.*

**Question 8:** Create a base class `Shape` with a method `area()` that simply returns `0`. Create two subclasses: `Rectangle` (takes `width` and `height`) and `Circle` (takes `radius`). Override the `area()` method in both subclasses to return their actual mathematical areas (For circle, use `3.14 * radius * radius`).

**Question 9:** Create a base class called `Entity`. It should have an attribute `hp` (health points). Add a method called `is_alive()` that returns `True` if `hp > 0`, and `False` otherwise.

**Question 10: BOSS LEVEL (The RPG Battle Engine)**
Create a `Player` class and a `Monster` class. **Both** must inherit from `Entity`.
* The `Player` `__init__` takes `name`, `hp`, and `stamina`. 
* The `Monster` `__init__` takes `name`, `hp`, and `rage_mode` (a boolean starting at `False`).
* Add an `attack(target)` method to `Player`: It reduces the `target.hp` by 20, and reduces the Player's `stamina` by 10. If the player has 0 stamina, they cannot attack (print a message instead).
* Add an `attack(target)` method to `Monster`: It reduces the `target.hp` by 15. **HOWEVER**, if the Monster's `hp` falls below 50, set `rage_mode = True`. If `rage_mode` is `True`, the Monster deals 30 damage instead of 15!

*The Test:* Instantiate a Player with 100 HP and a Monster with 100 HP. Write a `while` loop that makes them attack each other until one of them is no longer `is_alive()`. Print the winner!
