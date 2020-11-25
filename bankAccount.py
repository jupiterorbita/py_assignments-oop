class BankAcount:
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
  
chekingAccount = BankAcount(0.02, 100)
savingsAccount = BankAcount(0.05)

chekingAccount.display_account_info()
savingsAccount.display_account_info()


# To the first account, make 3 deposits and 1 withdrawal, then yield interest and display the account's info all in one line of code (i.e. chaining)
chekingAccount.deposit(100).deposit(200).deposit(50).widthdraw(150).yield_interest().display_account_info()

# To the second account, make 2 deposits and 4 withdrawals, then yield interest and display the account's info all in one line of code (i.e. chaining)
savingsAccount.deposit(2500).deposit(1000).widthdraw(1300).widthdraw(300).widthdraw(250).widthdraw(340).yield_interest()


# savingsAccount.deposit(100).yield_interest().display_account_info()