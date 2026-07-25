# 🏦 The Banking System (Mini OOP Project)

**Goal:** Combine everything you have learned (Classes, Inheritance, Encapsulation, `@classmethod`, and `super()`) into a single, functional banking system.

**Time Limit:** 45 Minutes. You are forbidden from asking for help during this time. Attempt the logic yourself. 

## System Requirements

You are to build two classes: `User` and `Bank`.

### 1. The `User` Class (Base Class)
- **Initialization:** Must store a user's `name`, `age`, and `gender`.
- **Method:** Create a `show_details()` method that returns a formatted string containing the user's name, age, and gender.

### 2. The `Bank` Class (Child Class)
- **Inheritance:** Must inherit from the `User` class.
- **Initialization:** Must take `name`, `age`, and `gender` and pass them to the parent class using `super()`.
- **Encapsulation:** Must initialize a **private** attribute called `__balance` starting at 0.
- **Class Attribute:** Create a class attribute called `total_accounts` starting at 0. Every time a new `Bank` object is created, this number should increase by 1.

### 3. Bank Operations (Methods inside the Bank Class)
- **`deposit(amount)`:** Adds the amount to the private balance and returns a success message showing the new balance.
- **`withdraw(amount)`:** Checks if there is enough money in the balance. If there is, subtract the amount and return a success message. If there is NOT enough money, return `"Insufficient Funds!"`.
- **`@property balance`:** Create a read-only getter to safely return the private `__balance`.
- **`@classmethod show_total_accounts()`:** Create a class method that returns the `total_accounts` class attribute.

---

### Verification
Once you build the system, run this exact script at the bottom of your file to prove it works:

```python
# 1. Create two accounts
account1 = Bank("Aryan", 16, "Male")
account2 = Bank("Elon", 53, "Male")

# 2. Test the methods on account1
print(account1.show_details())
print(account1.deposit(5000))
print(account1.withdraw(2000))
print(account1.withdraw(10000)) # Should fail

# 3. Test Encapsulation
print(f"Current Balance: {account1.balance}")

# 4. Test the Class Method
print(f"Total Bank Accounts Created: {Bank.show_total_accounts()}")
```
