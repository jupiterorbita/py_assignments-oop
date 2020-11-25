class User:
  def __init__(self, name, email):
    self.name = name
    self.email = email
    self.account_balance = 0
  def make_deposit(self, amount):
    self.account_balance += amount
  def make_withdrawal(self, amount):
    self.account_balance -= amount
  def display_user_balance(self):
    print(f"User {self.name}, Balance = ${self.account_balance}")
  def transfer_money(self, target, amount):
    print(f'{self.name} is transfering ${amount} to {target.name}')
    # self.target = target
    # self.amount = amount
    target.make_deposit(amount)
    target.display_user_balance()
    self.account_balance -= amount
    self.display_user_balance()
    # pass
    
# Create 3 instances of the User class
william = User('William', 'will@email.com')
jenny = User('Jenny', 'jen@email.com')
bill = User('Billy', 'billy@email.com')

# Have the first user make 3 deposits and 1 withdrawal and then display their balance
# william.make_deposit(100)
# william.make_deposit(25)
# william.make_deposit(55)
# william.display_user_balance()

# Have the second user make 2 deposits and 2 withdrawals and then display their balance
# jenny.make_deposit(350)
# jenny.make_deposit(450)
# jenny.make_withdrawal(100)
# jenny.make_withdrawal(500)
# jenny.display_user_balance()

# Have the third user make 1 deposits and 3 withdrawals and then display their balance
# bill.make_deposit(200)
# bill.make_withdrawal(10)
# bill.make_withdrawal(10)
# bill.make_withdrawal(200)
# bill.display_user_balance()

# BONUS: Add a transfer_money method; have the first user transfer money to the third user and then print both users' balances
william.transfer_money(bill, 100)