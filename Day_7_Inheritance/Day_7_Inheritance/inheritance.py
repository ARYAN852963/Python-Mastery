# 1.
class Device:
    def __init__(self, brand):
        self.brand = brand
        pass
class Phone(Device):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model
class SmartPhone(Phone):
    def __init__(self, brand, model, os):
        super().__init__(brand, model)
        self.os = os

a = SmartPhone("Apple", "Iphone 17", "IOS")
print(a.brand)
print(a.model)
print(a.os)

# 2.
class Vehicle:
    def __init__(self):
        pass
class Car(Vehicle):
    pass
class Bike(Vehicle):
    pass

# 3.
class Camera:
    def take_photo(self):
        print("Taking Photo")
class Phone:
    def make_call(self):
        print("Making Call")
class SmartPhone(Camera, Phone):
    pass
my_phone = SmartPhone()
my_phone.take_photo()
my_phone.make_call()
# 4.
class BankAccount:
    def __init__(self):
        self.__balance = 0  # This creates the private vault

    @property
    def balance(self,):
       return self.__balance 

my_account = BankAccount()
print(my_account.balance)

# 5.
class student:
    School = "Kendriya Vidyalaya"
    @classmethod
    def School(cls, new_school):
       cls.School = new_school

student.School("AFS JAMMU")
print(student.School)

# 6.
class MathsUtils:
    @staticmethod
    def number(number):
        if number % 2 == 0:
            return True
        else:
            return False
x = MathsUtils.number(100)
print(x)
# 7.
class Device:
    def __init__(self, brand):
        self.brand = brand
        pass
class Phone(Device):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model
class SmartPhone(Phone):
    def __init__(self, brand, model, os):
        super().__init__(brand, model)
        self.os = os

a = SmartPhone("Apple", "Iphone 17", "IOS")

print(isinstance(a, SmartPhone))
print(issubclass(SmartPhone, Device))

# 8.
class Employee:
    def calculated_salary(self):
        return 50000
    
class Manager(Employee):
    def calculated_salary(self):
        return super().calculated_salary() + 20000
a = Manager()
x = a.calculated_salary()  # Call the object, and use parentheses!
print(x)

# 9.
class Employee:
    def calculated_salary(self):
            return 50000
    def __init__(self,name):
        self.name = name
    def __str__(self,):
        return f"Employee Profile: {self.name}, Salary: {self.calculated_salary()}"

class Manager(Employee):
    def calculated_salary(self):
        return super().calculated_salary() + 20000
a = Employee("Aryan")
print(a)

# 10
class Vector:
    def __init__(self, x , y):
        self.x = x
        self.y = y
    def __add__(self, other):
        return Vector(self.x + other.x,  self.y + other.y)

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

v1 = Vector(2, 4)
v2 = Vector(1, 3)
v3 = v1 + v2
print(v3)
