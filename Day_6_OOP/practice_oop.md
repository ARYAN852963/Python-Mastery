# Day 6: Object Oriented Programming (OOP)

**MANDATORY RULE IN EFFECT:** The Time-Limit Anti-Cheat Rule.
- You must attempt each question for the specified time limit BEFORE asking for help.
- I will only give you HINTS, never the full answer. You must build the logic yourself.

## Level 1: OOP Fundamentals
**1. The Blueprint [Time Limit: 5 mins]**
Create a class called `Superhero`. Give it an `__init__` method that accepts `name` and `power`. Create an object `hero1` (e.g., Batman, Wealth) and print `hero1.name`.

**2. The First Method [Time Limit: 5 mins]**
Add a method `use_power(self)` to the `Superhero` class. It should print `"{name} uses {power}!"`. Call the method on `hero1`.

**3. The Multi-Object System [Time Limit: 5 mins]**
Create a second `Superhero` object (`hero2`) with different stats. Call `use_power()` on both `hero1` and `hero2` to prove they are independent objects.

## Level 2: State and Variables
**4. The Universe Counter [Time Limit: 10 mins]**
Add a Class Variable `hero_count = 0` to the top of the `Superhero` class (outside `__init__`). Inside the `__init__` method, every time a hero is created, add `1` to `Superhero.hero_count`. Create 3 heroes and print `Superhero.hero_count`.

**5. The Power Up [Time Limit: 10 mins]**
Add a method `upgrade_power(self, new_power)` to the `Superhero` class. It should change the hero's power to the `new_power`. Upgrade `hero1`'s power and call `use_power()` to prove it changed.

## Level 3: Encapsulation & Logic
**6. The Bank Account [Time Limit: 10 mins]**
Create a new class `BankAccount`. Its `__init__` should take an `owner` name, and set `self.balance = 0`. Create a `deposit(self, amount)` method that adds the amount to the balance. Create an account, deposit 500, and print the balance.

**7. The Strict Banker [Time Limit: 15 mins]**
Add a `withdraw(self, amount)` method to `BankAccount`. Add logic: if the amount is greater than the balance, print `"Insufficient Funds"`. Otherwise, subtract the amount from the balance. Test a successful withdrawal and a failed withdrawal.

## Level 4: Interacting Systems
**8. The Team Manager [Time Limit: 15 mins]**
Create a class called `Team`. Its `__init__` should create an empty list: `self.members = []`. 

**9. The Recruiter [Time Limit: 10 mins]**
Add a method `add_member(self, hero_name)` to `Team` that appends the name to `self.members`. Add a `show_team(self)` method that loops through `self.members` and prints each name. Create a Team, add 2 heroes, and show the team.

## Level 5: Boss Level
**10. The Battle Arena [Time Limit: 25 mins]**
Combine everything.
1. Create a class `Fighter` with `name`, `hp`, and `damage`.
2. Create an `attack(self, target)` method. 
3. When `fighter1.attack(fighter2)` is called, it should subtract `fighter1.damage` from `target.hp` and print `"{fighter1.name} attacks {target.name} for {damage} damage!"`
4. Create two fighters (e.g., Goku: 100 HP, 20 Dmg. Vegeta: 100 HP, 15 Dmg).
5. Have Goku attack Vegeta. Then print Vegeta's remaining HP to prove the math worked.
