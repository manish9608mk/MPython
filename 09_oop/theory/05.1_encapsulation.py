# Encapsulation

class Bank:

  def __init__(self, name:str, balance:int):
    self.name = name
    self.balance = balance

  def deposit(self, amount:int):
    self.balance += amount
    print(f'Amount deposited, current balance = {self.balance}')

  def withdraw(self, amount):
    if amount > self.balance:
      print('Not enough money in account')
    else:
      self.balance -= amount
      print(f'Amount withdrawn, current balance = {self.balance}')


acc = Bank('Manish',1000)
acc.deposit(2000)

acc.balance = 100000000

acc.withdraw(500)

# Public attributes can be changed directly from outside the class.




print()

class Bank:

  def __init__(self, name:str, balance:int):
    self.name = name

    # Private attribute
    self.__balance:int = balance

  # Getter
  def get_balance(self):
    print(f'Current balance is {self.__balance}')

  # Setter
  def set_balance(self, new_amount):
    if new_amount >= 0:
      self.__balance = new_amount

  # Private method
  def __isServerLive(self):
    return True

  def deposit(self, amount:int):
    if self.__isServerLive():
      self.__balance += amount
      print(f'Amount deposited, current balance = {self.__balance}')
    else:
      print('Server is down')

  def withdraw(self, amount):
    if amount > self.__balance:
      print('Not enough money in account')
    else:
      self.__balance -= amount
      print(f'Amount withdrawn, current balance = {self.__balance}')


acc = Bank('Manish',1000)

acc.deposit(2000)

acc.balance = 100000000
acc.__balance = 100000000

acc.withdraw(500)
acc.get_balance()

acc.set_balance(5000)
acc.get_balance()


# Private methods cannot normally be accessed
# using their original name from outside.
# acc.__isServerLive()  # AttributeError 