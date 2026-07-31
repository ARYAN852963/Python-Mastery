# Phase 2 Day 2: The Identity Theft Problem (`functools.wraps`)

> **⚠️ THE TIME-LIMIT ANTI-CHEAT RULE IS IN EFFECT ⚠️**
> Every practice question below has a strict time limit. During this time limit, you are FORBIDDEN from asking for help.

## The Theory (Read this or ask ChatGPT)
When you use a basic decorator, you create an inner `wrapper` function.
The problem? The original function's identity gets **stolen**. Its name (`__name__`) and its docstring (`__doc__`) are replaced by the wrapper's name and docstring. 

When you build Web Servers (like FastAPI), the server looks at the function's `__name__` to figure out the URL route (like `/login`). If all your decorated functions are named `"inner"`, the server crashes.

**The Solution:** Use `@functools.wraps(func)` inside your decorator, right above the `inner` function. It copies the original function's identity back.

```python
import functools

def my_decorator(func):
    @functools.wraps(func)  # <--- THIS IS THE MAGIC LINE
    def inner(*args, **kwargs):
        return func(*args, **kwargs)
    return inner
```

---

## Q1: The Identity Crisis (Warmup)
**Time Limit: 5 Minutes**
Write a decorator `bad_logger` (**without** using `wraps`). Apply it to a function `calculate_tax()` that has a docstring `"""Calculates tax"""`. Print `calculate_tax.__name__` and `calculate_tax.__doc__`. Notice how it prints the wrapper's name.

## Q2: The Hero's Return (Warmup)
**Time Limit: 5 Minutes**
Import `functools`. Write a new decorator `good_logger`. This time, use `@functools.wraps(func)` on the inner wrapper. Apply it to `calculate_discount()`. Print the name and docstring again to prove it kept its true identity.

## Q3: The Metadata Sniffer (Warmup)
**Time Limit: 5 Minutes**
Create a function `get_metadata(func)`. It should take a function as an argument, and print `"Name: [name], Doc: [doc]"`. Pass the functions from Q1 and Q2 into this sniffer to see the difference programmatically.

## Q4: The Docstring Extractor (1% Harder)
**Time Limit: 10 Minutes**
Write a decorator `@print_docs` (using `wraps`). Before the original function executes, it must print the original function's `__doc__`. If the original function has no docstring, it should print `"No documentation provided."`

## Q5: The Deprecation Warning (1% Harder)
**Time Limit: 10 Minutes**
Write a decorator `@deprecated` (using `wraps`). Before the function runs, it must print `WARNING: The function <function_name> is deprecated and will be removed soon.` Use `func.__name__` dynamically in the f-string.

## Q6: The Execution Log (1% Harder)
**Time Limit: 15 Minutes**
Create a global list `execution_log = []`. Write a decorator `@log_execution` (using `wraps`). Every time the function runs, append a string to the list: `"<function_name> was executed."` Apply it to 3 different functions and print the list.

## Q7: The Type Enforcer + Metadata (1% Harder)
**Time Limit: 15 Minutes**
Combine yesterday's logic with today's. Write `@only_strings` (using `wraps`). It must check if all `*args` are strings. If not, raise `TypeError`. Ensure the function keeps its real `__name__`.

## Q8: The Dictionary Router (1% Harder)
**Time Limit: 15 Minutes**
Create a dictionary `ROUTES = {}`. Write a decorator `@register` (using `wraps`). INSIDE the decorator (before the inner function is even defined), it should add the function to the dictionary like this: `ROUTES[func.__name__] = func`. 

## Q9: The Route Verifier (1% Harder)
**Time Limit: 20 Minutes**
Using the `ROUTES` dict from Q8. Write a function `trigger_route(url)`. If the `url` string exists as a key in `ROUTES`, execute the function stored there. If not, print `"404: Route Not Found"`.

## Q10: Boss Level - The Complete API Simulation
**Time Limit: 30 Minutes**
Imagine a real web server.
1. Create `API_ROUTES = {}`.
2. Write `@timer` (using `wraps`) that prints execution time.
3. Write `@api_route` (using `wraps`) that registers the function into `API_ROUTES`.
4. Create two functions: `get_users()` and `get_posts()`. 
5. Stack BOTH decorators on BOTH functions. 
6. **CRITICAL:** What order should you stack them so that `API_ROUTES` stores the timed version of the function, BUT the key in the dictionary is exactly `"get_users"` and not `"inner"`? Prove it works by printing the keys of `API_ROUTES`.
