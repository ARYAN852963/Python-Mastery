# 1.
def multiply(a, b):
    return a*b
answer = multiply(10, 20)
print(answer)
# 2.
def get_welcome_message(name):
    return f"Welcome to the system, {name}!"

print(get_welcome_message("Aryan"))
# 3.
def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False
x = is_even(1000)
print(x)
# 4.
def multiply(a, b):
    return a*b
def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False
x = is_even(multiply(4, 5))
print(x)
# 5.
company = "OpenAI"
def change_company():
    company = "DeepMind"
    return company
x = change_company()
print(x)
print(company)
# 6.
counter = 0
def increment():
    global counter
    counter += 1
increment()
increment()
increment()
print(counter)
# 7.
def calculate_total(price):
    tax = 0.20
    return price + (price * tax)

x = calculate_total(100)
print(x)
# 8.
class ShoppingCart:
    def __init__(self):
        self.__items = []

    def add_item(self, item_name):
        self.__items.append(item_name)
        return "Item Added"
    def get_items(self):
        return self.__items

cart = ShoppingCart()

print(cart.add_item("Apple"))
print(cart.add_item("Milk"))
print(cart.add_item("Bread"))        
print(cart.get_items())