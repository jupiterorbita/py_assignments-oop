# Assignment: Users with Bank Accounts
# -------------- USERS CLASS -------------
class User:
  def __init__(self, name, email):
    self.name = name
    self.email = email
    self.account = BankAccount(int_rate=0.02, balance=0 )
  def make_deposit(self, amount):
    self.account.deposit(amount)
    print(f'{self.name} deposited ${self.account.balance}')
    return self
  def make_withdrawal(self, amount):
    self.account.widthdraw(amount)
    print(f'{self.name} withdrew ${self.account.balance}')
    return self
  def display_user_balance(self):
    print(f'{self.name}, your balance is ${self.account.balance} > User.display_user_balance()')
  #   print(self.account.display_account_info())
  #   # print(f"User {self.name}, Balance = ${self.account.display_account_info()}\n")
    return self
  def transfer_money(self, target, amount):
    print(f'{self.name} is transfering ${amount} to {target.name}')
    # self.target = target
    # self.amount = amount
    target.make_deposit(amount)
    # target.display_user_balance()
    # target.account.display_account_info()
    self.account.widthdraw(amount)
    self.account.display_account_info()
    return self
    # pass

# ============ BANK CLASS ================
class BankAccount:
  def __init__(self, int_rate, balance=0):
    self.balance = balance
    self.int_rate = float(int_rate)
  def deposit(self, amount):
    self.balance += amount
    return self
  def widthdraw(self, amount):
    self.balance -= amount
    return self
  def display_account_info(self):
    print(f'your balance is ${self.balance}, interest rate is {self.int_rate*100}%')
    return self
  def yield_interest(self):
    self.balance += self.balance * self.int_rate
    self.display_account_info()
    return self
# Create 3 instances of the User class
william = User('William', 'will@email.com')
jenny = User('Jenny', 'jen@email.com')
bill = User('Billy', 'billy@email.com')

# william.account(0.05, 100)
# print(william)
# william.make_deposit(100).display_user_balance()
print()
william.make_deposit(100).account.display_account_info()
# print(william.display_user_balance())
# print(william.account.display_account_info())
print('-'*30)
william.transfer_money(jenny, 50)
# jenny.account.display_account_info()
jenny.display_user_balance()