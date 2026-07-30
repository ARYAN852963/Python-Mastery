# 1.
def do_nothing(func):
    def inner(*args, **kwargs):
        result = func(*args, **kwargs)
        return result
    return inner
@do_nothing
def add(*args, **kwargs):
    return args[0] + args[1]
print(add(10, 20))

# 2.
def annouce(func):
    def inner(*agrs, **kwargs):
        print("Executing function.....")
        result = func(*agrs, **kwargs)
        print(result)
        print("Function Executed....")
    return inner
@annouce
def add(*args, **kwargs):
    return args[0] + args[1]
add(10, 20)
# 3.
def log_args(func):
    def inner(*args, **kwargs):
        print(args)
        print(kwargs)
        result = func(*args, **kwargs)
        return result
    return inner
@log_args
def greet(*args, **kwargs):
    pass
greet("Aryan", 16, city="Jammu", country="India")
# 4.
def make_uppercase(func):
    def inner(*args, **kwargs):
        result = func(*args, **kwargs)
        if isinstance(result, str):
            return result.upper()
        else:
            return result
    return inner
@make_uppercase
def string():
    return "kallu"
print(string())
# 5.
def only_integers(func):
    def inner(*args, **kwargs):
        for value in args:
            if not isinstance(value, int):
                raise TypeError("Only integers allowded!!")
        result = func(*args, **kwargs)
        return result 
    return inner
@only_integers
def add(a, b):
    return a + b
print(add(10, 15))
print(add(10 , 15))
# 6.
def safe_execute(func):
    def inner(*args, **kwargs):
        try:
         result = func(*args,**kwargs)
         return result
        except Exception:
            print("Function Failed")
            return -1
    return inner
@safe_execute
def divide(a,b):
    return a/b
print(divide(10, 20))
print(divide(20, 0))
print(divide(20,10))
# 7.
import time
def timer(func):
    def inner(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"It took {end-start}second!. ")
        return result
    return inner
@timer
def test():
    for i in range (1000000):
        pass
    return test
test()
# 8.
def retry_once(func):
    def inner(*args, **kwargs):
        try:
            return func(*args , **kwargs )   
        except Exception:
            print("Retrying....")
            return func(*args, **kwargs)
    return inner
@retry_once
def divide(a, b):
    return a / b

print(divide(10, 2))   
print(divide(10, 10))
# 9.
ACTIVE_USER = {"role": "Admin"}
def admin_only(func):
    def inner(*args, **kwargs):
        if ACTIVE_USER["role"] != "Admin":
            raise PermissionError
        else:
            result = func(*args, **kwargs)
            return result
    return inner
@admin_only
def check():
    print("Welcome, Admin!")
check()
# 10
import time
def timer(func):
    def inner(*args, **kwargs):
        start = time.time()

        result = func(*args, **kwargs)

        end = time.time()
        print(f"Function took {end - start:.6f} seconds")

        return result
    return inner
def retry_once(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception:
            print("Retrying...")
            return func(*args, **kwargs)
    return inner
def safe_execute(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception:
            print("Function failed")
            return -1
    return inner
attempt = 0 
@timer
@safe_execute
@retry_once
def fetch_data():
    global attempt 
    attempt += 1
    print(f"It took {attempt} attempts!")
    if attempt <= 2:
        raise Exception("Sever Error")
    return "Data received"


print(fetch_data())