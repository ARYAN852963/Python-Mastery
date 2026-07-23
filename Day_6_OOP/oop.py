# Day 6: Object Oriented Programming (OOP)
# ----------------------------------------

# 1. 
# class superhero:
#     def __init__ (self, name, power):
#         self.name = name
#         self.power = power
# hero1 = superhero("Batman", "Spider_web")
# print(hero1.name)

# 2.
# class superhero:
#     def __init__ (self, name, power):
#         self.name = name
#         self.power = power
#     def use_power(self):
#         print(f"{self.name} uses {self.power}!")
    
# hero1 = superhero("Batman", "Spider_web")
# hero1.use_power()

# 3.
# class superhero:
#     def __init__ (self, name, power):
#         self.name = name
#         self.power = power
#     def use_power(self):
#         print(f"{self.name} uses {self.power}!")
    
# hero1 = superhero("Batman", "Spider_web")
# hero2 = superhero("Aryan", "Coding")
# hero1.use_power()
# hero2.use_power()

# 4.
# class superhero:
#     hero_count = 0
#     def __init__ (self, name, power):
#         self.name = name
#         self.power = power
#         superhero.hero_count = superhero.hero_count + 1
#     def use_power(self):
#         print(f"{self.name} uses {self.power}!")
# hero1 = superhero("Batman", "Spider_web")
# hero2 = superhero("Aryan", "Coding")
# hero1.use_power()
# hero2.use_power()
# print(superhero.hero_count)

# 5.
# class superhero:
#     hero_count = 0
#     def __init__ (self, name, power):
#         self.name = name
#         self.power = power
#         superhero.hero_count = superhero.hero_count + 1
#     def use_power(self):
#         print(f"{self.name} uses {self.power}!")
#     def upgrade_power(self, new_power):
#         self.power = new_power
#         print(f"{self.name}'s power has been upgraded!")
# hero1 = superhero("Batman", "Spider_web")
# hero1.upgrade_power("Flying")
# hero2 = superhero("Aryan", "Coding")
# hero1.use_power()
# hero2.use_power()
# print(superhero.hero_count)

# 6.
# class BankAccount:
#     def __init__(self, Name, balance ):
#         self.Name = Name
#         self.balance = balance
#     def deposit(self, amount):
#         self.balance = self.balance + amount
#         print(f"Your balance is {self.balance}")
# Account1 = BankAccount("Aryan", 0)
# Account1.deposit(1000008)

#7.
# class BankAccount:
#     def __init__(self, Name, balance ):
#         self.Name = Name
#         self.balance = balance
#     def deposit(self, amount):
#         self.balance = self.balance + amount
#         print(f"Your balance is {self.balance}")
#     def withdraw(self, amount):
#         self.amount = amount
#         if amount > self.balance:
#             print("Insufficient Funds")
#         elif amount < self.balance:
#             print(f"Your balance is {self.balance - amount}")
#         else:
#             print("Error")
# Account1 = BankAccount("Aryan", 0)
# Account1.deposit(100000)
# Account1.withdraw(50000)

# 9.
class team:
    def __init__(self):
        self.members = []
    def add_member(self, hero_name):
        self.members.append(hero_name)
    def show_team(self):
        for i in self.members:
            print(i)

my_team = team() # Build the empty team
my_team.add_member("Alice") # Add the first member
my_team.add_member("Bob") # Add the second member
my_team.show_team() # Show the team!

# 10.
class Fighter:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage

    def attack(self, target):
        target.hp = target.hp - self.damage
        print(f"{self.name} attacks {target.name} for {self.damage} damage!")


# Create two fighters
fighter1 = Fighter("Goku", 100, 20)
fighter2 = Fighter("Vegeta", 100, 15)

# Goku attacks Vegeta
fighter1.attack(fighter2)

# Print Vegeta's remaining HP
print(f"{fighter2.name}'s remaining HP is {fighter2.hp}")

