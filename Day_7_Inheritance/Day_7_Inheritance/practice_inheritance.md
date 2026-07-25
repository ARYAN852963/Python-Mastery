# Day 7: The OOP Final Exam (Green Ticks + Dunder)

**Time Limit: 60 Minutes**
*Rule: Do not ask for help until the timer rings. Provide the raw code to satisfy the system requirements below.*

## Level 1: The Inheritance Web
*Testing: Single, Multilevel, Multiple, and Hierarchical Inheritance.*

**Question 1 (Multilevel):** Build a `Device` class with a `brand` attribute. Build a `Phone` class that inherits from `Device` and adds a `model` attribute. Build a `SmartPhone` class that inherits from `Phone` and adds an `os` attribute. Use `super()` correctly at every level.
**Question 2 (Hierarchical):** Build a base `Vehicle` class. Build two separate subclasses, `Car` and `Bike`, that both inherit from `Vehicle`.
**Question 3 (Multiple):** Build a `Camera` class with a `take_photo()` method. Build a `Phone` class with a `make_call()` method. Build a `SmartPhone` class that inherits from BOTH `Camera` and `Phone`. Instantiate a `SmartPhone` and prove it can use both methods.

---

## Level 2: The Core Mechanics
*Testing: Encapsulation, Class Methods, Static Methods, and Built-ins.*

**Question 4 (Encapsulation):** Build a `BankAccount` class with a **private** attribute `__balance`. It should be impossible to modify `__balance` directly from outside the class. Write a property (getter) to read the balance, and a method to deposit money.
**Question 5 (@classmethod):** Build a `Student` class with a class attribute `school_name = "Kendriya Vidyalaya"`. Write a `@classmethod` called `change_school()` that changes the school name for ALL students at once.
**Question 6 (@staticmethod):** Build a `MathUtils` class. Write a `@staticmethod` called `is_even(number)` that returns `True` if a number is even, and `False` otherwise. You should be able to call this without instantiating the class.
**Question 7 (isinstance & issubclass):** Write a script that proves (using `isinstance()`) that your `SmartPhone` object from Question 1 is indeed a `Device`. Then use `issubclass()` to prove that `SmartPhone` is a subclass of `Device`.

---

## Level 3: The Dunder Boss Level
*Testing: Method Overriding and Dunder (Magic) Methods.*

**Question 8 (Overriding):** Build an `Employee` class with a `calculate_salary()` method that returns a base salary of 50,000. Build a `Manager` class that overrides this method to return the base salary PLUS a 20,000 bonus.
**Question 9 (The `__str__` Dunder):** Update your `Employee` class by adding the `__str__` dunder method. When you run `print(employee_object)`, it should output exactly: `"Employee Profile: [Name], Salary: [Salary]"`.
**Question 10: BOSS LEVEL (The `__add__` Dunder):**
Build a `Vector` class that takes two coordinates, `x` and `y`.
Implement the `__add__` dunder method.
Your system must allow me to instantiate two vectors: `v1 = Vector(2, 3)` and `v2 = Vector(4, 1)`.
When I run `v3 = v1 + v2`, the system should combine their coordinates so that `v3.x` is 6 and `v3.y` is 4.
