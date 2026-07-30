# Phase 2 Day 1: Simple Decorator Mechanics (Day 1 of 4)

> **⚠️ THE TIME-LIMIT ANTI-CHEAT RULE IS IN EFFECT ⚠️**
> Every practice question below has a strict time limit. 
> During this time limit, you are FORBIDDEN from asking me (the AI) for help. You must attempt to write the logic and debug entirely on your own. 
> Only AFTER the time limit has expired, if you are stuck or have an error, you may ask for a small hint.

**Focus:** Today is strictly about muscle memory for the basic syntax. No `functools.wraps`, no parameterized decorators (passing arguments to the decorator itself), no classes. Just `def decorator(func):`, `def wrapper(*args, **kwargs):`, and returning the wrapper.

## Q1: The Pass-Through (Warmup)
**Time Limit: 5 Minutes**
**System Requirements:**
Create a decorator `do_nothing`. It should take a function, define an inner wrapper that accepts `*args` and `**kwargs`, call the original function with those arguments, and return the result. This is the baseline skeleton for all decorators.

## Q2: The Announcer (Warmup)
**Time Limit: 5 Minutes**
**System Requirements:**
Create a decorator `announce`. It must print "Executing function..." before the decorated function runs, and "Execution complete." after it finishes. Apply it to a simple function that adds two numbers.

## Q3: The Argument Sniffer (Warmup)
**Time Limit: 10 Minutes**
**System Requirements:**
Create a decorator `log_args`. It must print the exact `args` tuple and `kwargs` dictionary to the terminal before the function executes. It must return the original function's result unaltered.

## Q4: The Output Transformer (1% Harder)
**Time Limit: 10 Minutes**
**System Requirements:**
Create a decorator `make_uppercase`. It must intercept the return value of the original function. If the return value is a string, it must convert it to uppercase and return that instead. If it's not a string, return it unaltered.

## Q5: The Basic Type Guard (1% Harder)
**Time Limit: 15 Minutes**
**System Requirements:**
Create a decorator `only_integers`. It must loop through all positional `args`. If any argument is not of type `int`, it must immediately raise a `TypeError("Only integers allowed")` without running the function.

## Q6: The Fallback Value (1% Harder)
**Time Limit: 15 Minutes**
**System Requirements:**
Create a decorator `safe_execute`. Wrap the original function's execution in a `try...except Exception` block. If the function crashes, catch the exception, print "Function failed", and return the integer `-1` instead of crashing the program.

## Q7: The Execution Profiler (1% Harder)
**Time Limit: 15 Minutes**
**System Requirements:**
Create a decorator `timer`. Record the exact time before and after the function runs using the `time` module. Print "Function took X seconds". Ensure the original function's return value is not lost.

## Q8: The Simple Retry (1% Harder)
**Time Limit: 20 Minutes**
**System Requirements:**
    Create a decorator `retry_once`. If the wrapped function throws an exception, catch it, print "Retrying...", and execute the function exactly one more time. If it fails on the second try, allow the exception to crash the program naturally.

## Q9: The Global Authorization Gate (1% Harder)
**Time Limit: 20 Minutes**
**System Requirements:**
Create a global variable dictionary: `ACTIVE_USER = {"role": "guest"}`. 
Create a decorator `admin_only`. Before running the function, it must check `ACTIVE_USER["role"]`. If the role is not `"admin"`, raise a `PermissionError`. If it is `"admin"`, run the function.

## Q10: Boss Level - The Decorator Stack
**Time Limit: 30 Minutes**
**System Requirements:**
You must apply THREE of your previous decorators to a single flaky function `fetch_data()`: `@timer`, `@retry_once`, and `@safe_execute`.
Your task: Determine the exact order these decorators should be stacked above the function so that:
1. The execution time is measured for the ENTIRE process (including the time taken by the retry).
2. If it fails twice, the fallback value `-1` is returned, and the program does not crash.
Write the code and stack them to prove your order works.
