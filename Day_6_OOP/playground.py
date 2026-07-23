# Day 6 OOP Playground
# Use this file to test out classes, methods, and objects!

# Example 1: The Basics of a Class
class techStartup:
    # The __init__ method is the "constructor". It builds the object.
    def __init__(self, company_name, industry):
        self.name = company_name
        self.industry = industry
        self.revenue = 0  # Default value
        
    def make_sale(self, amount):
        self.revenue += amount
        print(f"{self.name} just made ${amount}! Total revenue: ${self.revenue}")

# Try creating your own startup object below!
# my_startup = TechStartup("Aryan AI", "Artificial Intelligence")
# my_startup.make_sale(500)
class TechStartup:
    # The __init__ method is the "constructor". It builds the object.
    def __init__(self, company_name, industry):
        self.name = company_name
        self.industry = industry
        self.revenue = 0  # Default value
        
    def make_sale(self, amount):
        self.revenue += amount
        print(f"{self.name} just made ${amount}! Total revenue: ${self.revenue}")
my_startup = TechStartup("Aryan AI", "Artificial Intelligence")
my_startup.make_sale(500)

# ---------------------------------------------------------
# Example 2: Objects Interacting (Like your Fighter class!)
# class Coder:
#     def __init__(self, name, energy):
#         self.name = name
#         self.energy = energy
#         self.lines_of_code = 0
        
#     def drink_coffee(self):
#         self.energy += 20
#         print(f"{self.name} drank coffee. Energy is now {self.energy}!")
        
#     def write_code(self):
#         if self.energy >= 10:
#             self.lines_of_code += 50
#             self.energy -= 10
#             print(f"{self.name} wrote 50 lines of code! Total: {self.lines_of_code}. Energy left: {self.energy}")
#         else:
#             print(f"{self.name} is too tired to code. Need coffee!")

# Test it out!
# aryan = Coder("Aryan", 15)
# aryan.write_code()
# aryan.write_code() # This should fail because energy < 10
# aryan.drink_coffee()
# aryan.write_code()
class coder:
    def __init__(self, name, energy):
        self.name = name
        self.energy = energy
        self.lines_of_code = 0
        
    def drink_coffee(self):
        self.energy += 20
        print(f"{self.name} drank coffee. Energy is now {self.energy}!")
        
    def write_code(self):
        if self.energy > 10:
            self.lines_of_code += 50
            self.energy -= 10
            print(f"{self.name} wrote 50 lines of code! Total: {self.lines_of_code}. Energy left: {self.energy}")
        else:
            print(f"{self.name} is too tired to code. Need coffee!")
aryan = coder("Aryan", 35)
aryan.write_code()
aryan.drink_coffee()
# ---------------------------------------------------------
# YOUR TURN:
# Build whatever class you want down here and test it!

