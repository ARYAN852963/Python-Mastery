class user:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age 
        self.gender = gender
        pass
    def show_details(self):
        return (
            f"--- User Details ---\n"
            f"Name   : {self.name}\n"
            f"Age    : {self.age}\n"
            f"Gender : {self.gender}"
        )
class bank(user):
    total_accounts = 0
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)
        self.__balance = 0
        bank.total_accounts +=1
    def deposit(self, amount):
         self.__balance += amount
         return f"Success! Deposited ₹{amount}. New Balance: ₹{self.__balance}"
    def withdraw(self, amount):
        if amount <= 0:
            return "Withdrawal amount must be greater than zero."
        if amount > self.__balance:
          return "Insufficient Funds!"
        self.__balance -= amount
        return f"Success! Withdrew ₹{amount}. New Balance: ₹{self.__balance}"
    @property
    def balance(self) -> float:
        """Read-only getter to safely view the private balance."""
        return self.__balance
    @classmethod
    def show_total_accounts(cls) -> int:
        """Class method returning the global total accounts tracking variable."""
        return cls.total_accounts

account1 = bank("Aryan", 16, "Male")
account2 = bank("Elon", 53, "Male")

# 2. Test the methods on account1
print(account1.show_details())
print(account1.deposit(5000))
print(account1.withdraw(2000))
print(account1.withdraw(10000)) # Should fail