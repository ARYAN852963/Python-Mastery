# Day 10: Error Handling & Advanced Arguments

# 1. Catching ValueError
try:
    year = int(input("Enter your birth year: "))
except ValueError:
    print("Add the year in the form of a Number!")

# 2. Catching IndexError
city = ["Jammu", "Gurugram", "Noida"]
try:
    number = int(input("Enter a number: "))
    print(city[number])
except IndexError:
    print("Give me the number from 0 to 2")
except Exception:
    print("An error occurred!")

# 3. Catching ZeroDivisionError & TypeError
def safe_divide(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        print("The denominator can't be zero!")
    except TypeError:
        print("You cannot divide a number by text!")

safe_divide(1, "n")

# 4. File Handling with finally
def read_file(filename):
    try:
        with open(filename, "r") as file:
            content = file.read()
            return content
    except FileNotFoundError:
        print("Warning: File not found!")
    finally:
        print("File read attempt finished")

read_file("ghost.txt")

# 5. Raising custom ValueError
def process_payment(amount):
    if amount < 0:
        raise ValueError("Your amount cannot be negative")
    return amount

try:
    process_payment(-10)
except ValueError as e:
    print(e)

# 6. Infinite Arguments (*args)
def sum_all(*args):
    total = 0
    for number in args:
        total += number
    return total

print("Sum:", sum_all(10, 20, 30, 90, 110))

# 7. Keyword Arguments (**kwargs)
def display_team(**kwargs):
    for key, value in kwargs.items():
        print(f"The {key} is {value}")

display_team(manager="Alice", developer="Bob", designer="Aryan")

# 8. Combined args and kwargs
def create_server_config(ip_address, *args, **kwargs):
    return f"Server IP: {ip_address}, Open Ports: {args}, Extra Settings: {kwargs}"

output = create_server_config("192.168.1.1", 8080, 443, 22, timeout=30, debug=True, max_users=100)
print(output)

# 9 & 10. The Boss Level (Architecture)
class Authenticator:
    def __init__(self):
        self.__banned_users = ["hacker123", "spammer99"]
        
    def login(self, username):
        if username in self.__banned_users:
            raise PermissionError(f"{username} is banned.")
        elif username == "":  
            raise ValueError("Username cannot be empty.")
        return "Login successful"

def bulk_register(*args):
    my_auth_system = Authenticator()
    for person in args:
        try:
            result = my_auth_system.login(person)
            print(f"Success for {person}: {result}")
        except PermissionError:
            print(f"WARNING: {person} is a BANNED HACKER!")
        except ValueError:
            print("WARNING: Someone tried to use an empty username!")

bulk_register("Aryan", "hacker123", "Elon", "", "spammer99", "Steve")