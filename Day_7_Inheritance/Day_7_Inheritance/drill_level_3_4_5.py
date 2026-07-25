class Warrior:
    def __init__(self):
        self.health = 100
        pass
    def take_damage(self):
        self.health -= 20

a = Warrior()
a.take_damage()
a.take_damage()

print(a.health)

# # 2.
# class BankAccount:
#     def __init__(self):
#         self.balance = 0
#     def deposit(self, amount):
#         self.balance += amount
#     def withdraw(self, amount):
#         self.balance -= amount
# b = BankAccount()
# b.deposit(40000)
# b.withdraw(1000)

# print(b.balance)

# 3.
class car:
    def __init__(self):
        self.speed = 0
    def accelerate(self, ammount):
        self.speed += ammount
    def brake(self, ammount):
        self.speed -= ammount
        if self.speed < 0:
            self.speed = 0
d = car()
d.accelerate(320)
d.brake(100)
print(d.speed)
# 4.
class Calculator:
    def add (self, a, b):
         return a+b
my_calc = Calculator()
x = my_calc.add(10, 5)
print(x)
# 5.
class Store:
    def calculate_tax(self, price):
        return (18/100)*price
a = Store()
amount = a.calculate_tax(2500)
print(amount + 50)
# 6.
class AgeVerifier:
    def isadult(self, age):
        if age >= 18:
            return True
        else:
            return False
s = AgeVerifier()
g = s.isadult(20)
print(g)
# 7.
class Character:
    def __init__(self, name, health):
        self.name = name
        self.health = health
class Mage(Character):
    def __init__(self, name, health, mana):
        super().__init__(name, health)
        self.mana = mana
# 9
class Animal():
    def make_sound(self):
        print("Some generic sound")
class Dog(Animal):
    def make_sound(self):
        return "BARK!"
A = Dog()
g = A.make_sound()
print(g)