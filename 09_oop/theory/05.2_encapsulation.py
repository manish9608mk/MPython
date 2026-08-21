'''
Encapsulation

Encapsulation means protecting the internal data of a class
and controlling how it can be accessed or modified.

Key points:
- Data and methods are bundled together inside a class.
- Sensitive data can be made private.
- Private data should not be accessed directly from outside.
- Getters are used to read private data.
- Setters are used to modify private data safely.
- It helps prevent accidental changes to important data.
- It makes code more secure and easier to maintain.

Access levels in Python:
- Public     → accessible from anywhere
- Protected  → intended for use inside the class and subclasses
- Private    → intended to be accessed through the class interface

Real-life example:
An ATM allows you to check your balance and withdraw money,
but you cannot directly access or modify the bank's internal system.

Example:
Class
├── Private data
├── Getter → safely read data
└── Setter → safely modify data
'''


# ============================================================
# M1 - Problem with a public attribute
# ============================================================

class Bank:

    def __init__(self, name: str, balance: int) -> None:
        self.name = name
        self.balance = balance

    def deposit(self, amount: int) -> None:
        self.balance += amount
        print(f'Amount deposited, current balance = {self.balance}')

    def withdraw(self, amount: int) -> None:
        if amount > self.balance:
            print('Not enough money in account')
        else:
            self.balance -= amount
            print(f'Amount withdrawn, current balance = {self.balance}')


acc = Bank('Manish', 1000)

acc.deposit(2000)

# Anyone can directly change the public balance.
# There is no control or validation here.
acc.balance = 100000000

acc.withdraw(500)

'''
Problem:

balance is public.

Anyone from outside the class can directly change it:

    acc.balance = 100000000

This can bypass the rules of the Bank class.

So, we should make balance private.
'''


print()


# ============================================================
# M2 - Encapsulation using a private attribute
# ============================================================

class Bank:

    def __init__(self, name: str, balance: int) -> None:
        self.name = name

        # Private attribute
        # __balance uses double underscore for name mangling.
        self.__balance: int = balance

    # Getter
    # Used to safely read the private balance.
    def get_balance(self) -> int:
        return self.__balance

    # Setter
    # Used to safely modify the private balance.
    # Validation can be added before changing the value.
    def set_balance(self, new_amount: int) -> None:
        if new_amount >= 0:
            self.__balance = new_amount
        else:
            print('Balance cannot be negative')

    # Private method
    # This method is intended for internal use inside the class.
    def __is_server_live(self) -> bool:
        return True

    def deposit(self, amount: int) -> None:

        # Internal method can access the private method.
        if self.__is_server_live():
            self.__balance += amount
            print(
                f'Amount deposited, current balance = {self.__balance}'
            )
        else:
            print('Server is down')

    def withdraw(self, amount: int) -> None:

        if amount > self.__balance:
            print('Not enough money in account')
        else:
            self.__balance -= amount
            print(
                f'Amount withdrawn, current balance = {self.__balance}'
            )


# ============================================================
# Creating an object
# ============================================================

acc = Bank('Manish', 1000)

acc.deposit(2000)

print(f'Current balance: {acc.get_balance()}')


# ============================================================
# Trying to access private data from outside
# ============================================================

# This does NOT modify the actual private __balance.
# It creates a separate public attribute named "balance".
acc.balance = 100000000

# This also does NOT modify the actual private __balance.
# Python uses name mangling for __balance.
acc.__balance = 100000000


acc.withdraw(500)

print(f'Actual private balance: {acc.get_balance()}')


# ============================================================
# Using the setter
# ============================================================

# We modify the private balance through the setter.
acc.set_balance(5000)

print(f'Balance after setter: {acc.get_balance()}')


# ============================================================
# Private method
# ============================================================

# This cannot normally be accessed using its original name:
#
# acc.__is_server_live()
#
# It would raise AttributeError because the method is private.


'''
Important:

Encapsulation
      ↓
Protect internal data
      ↓
Private attribute
      ↓
__balance
      ↓
Controlled access
      ↓
Getter + Setter


Bank
│
├── name                 ← public
│
├── __balance            ← private
│
├── get_balance()        ← getter
│
├── set_balance()        ← setter
│
├── deposit()            ← public method
│
├── withdraw()           ← public method
│
└── __is_server_live()   ← private method


Key interview point:

__balance is not completely inaccessible in Python.

Python uses NAME MANGLING:

    self.__balance

internally becomes approximately:

    self._Bank__balance

So double underscore provides name mangling,
not absolute security.
'''