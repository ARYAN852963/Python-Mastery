# 1.
def bad_logger(func):
    def inner(*args, **kwargs):
        print("Function is loading!")
        return func(*args, **kwargs)
    return inner
@bad_logger
def calculate_tax():
    """Calculates tax"""
    return 110
print(calculate_tax.__name__)
print(calculate_tax.__doc__)
# 2.
from functools import wraps
def good_logger(func):
    @wraps(func)
    def inner(*args, **kwargs):
        print("Function is loading!")
        return func(*args, **kwargs)
    return inner
@good_logger
def calculate_tax():
    """Calculates tax"""
    return 110
print(calculate_tax.__name__)
print(calculate_tax.__doc__)
# 3.
from functools import wraps

def bad_logger(func):
    def inner(*args, **kwargs):
        print("Function is loading!")
        return func(*args, **kwargs)
    return inner

@bad_logger
def calculate_tax():
    """Calculates tax"""
    return 110

def good_logger(func):
    @wraps(func)
    def inner(*args, **kwargs):
        print("Function is loading!")
        return func(*args, **kwargs)
    return inner

@good_logger
def calculate_tax():
    """Calculates tax"""
    return 110

def get_metadata(func):
      print(f"Name: {func.__name__}, Doc: {func.__doc__}")

get_metadata(calculate_tax)
# 4.
from functools import wraps
def print_docs(func):
    @wraps(func)
    def inner(*args, **kwargs):
        if func.__doc__:
            print(func.__doc__)
        else:
            print("No Docuentation provided")
        return func(*args, **kwargs)
    return inner
@print_docs
def greet():
    print("hello")
greet()
# 5.
from functools import wraps
def deprecated(func):
    @wraps(func)
    def inner(*args, **kwargs):
        print(f"WARNING: The function {func.__name__} is deprecated and will be removed soon.")
        return func(*args, **kwargs)
    return inner
@deprecated
def warning():
    print("Function is running")
warning()
# 6.
from functools import wraps
execution_log = []
def log_execution(func):

    wraps(func)
    def inner(*args, **kwargs):
        result  = func(*args, **kwargs)
        execution_log.append(f"{func.__name__} was executed.")
        return result
    return inner
@log_execution
def warning():
    return warning
@log_execution
def upload():
    return upload
@log_execution
def login():
    return login
warning()
upload()
login()
print(execution_log)
# 7.
from functools import wraps
def only_string(func):
    @wraps(func)
    def inner(*args, **kwargs):
        for value in args:
            if not isinstance(value, str):
                raise TypeError("Only string's allowded!!")
        result = func(*args, **kwargs)
        return result 
    return inner
@only_string
def add(a, b):
    return a + b
print(add("Aryan" , "Sharma"))
# 8.
from functools import wraps
ROUTES = {}
def register(func):
    ROUTES[func.__name__] = func
    @wraps(func)
    def inner(*args, **kwargs):
        return func(*args, **kwargs)
    return inner
def trigger_route(url):
 if url in ROUTES:
    return ROUTES[url]()
 else:
     print("404: Route Not Found")
@register
def home():
    print("Welcome to Home")


@register
def login():
    print("Welcome to Login")


@register
def about():
    print("About Us")


print(ROUTES)          # See what is stored

trigger_route("home")  # Runs home()
trigger_route("login") # Runs login()
trigger_route("about") # Runs about()
trigger_route("xyz")   # Route doesn't exist
# 10
from functools import wraps
from time import time

API_ROUTES = {}


def timer(func):
    @wraps(func)
    def inner(*args, **kwargs):
        start = time()

        result = func(*args, **kwargs)

        end = time()
        print(f"{func.__name__} took {end - start:.6f} seconds")

        return result

    return inner


def api_route(func):
    # Register the function
    API_ROUTES[func.__name__] = func

    @wraps(func)
    def inner(*args, **kwargs):
        return func(*args, **kwargs)

    return inner


@api_route
@timer
def get_users():
    print("Getting users...")


@api_route
@timer
def get_posts():
    print("Getting posts...")


print(API_ROUTES.keys())

API_ROUTES["get_users"]()
API_ROUTES["get_posts"]()


