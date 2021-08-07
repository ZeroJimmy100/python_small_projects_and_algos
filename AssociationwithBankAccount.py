class User:
    def __init__(self, username, email, other_user):
        self.name = username			
        self.email = email		
        self.account = BankAccount(int_rate=0.02, balance=0)     
        self.other_user = username
    def make_deposit(self, amount):	
    	self.account.balance += amount	
    def make_withdrawal(self, amount):
        self.account.balance -= amount
    def display_user_balance(self):
        BankBalance = {"User": self.name, "Balance": self.account.balance}
        print(BankBalance)
    def transfer_money(self, other_user, amount):
        self.account.balance -= amount
        other_user.account.balance += amount
class BankAccount:
	def __init__(self, int_rate, balance):
            self.int_rate = 0
            self.balance = 0

	def deposit(self, amount):
            self.balance += amount
            return self
		
	def withdraw(self, amount):
            self.balance -= amount
            if self.balance <= 0:
                self.balance -= 5
                self.balance -=5
            return self
		
	def display_account_info(self):
            BankBalance = {"Balance": self.balance}
            print(BankBalance)
            return self
		
	def yield_interest(self):
            if self.balance < 0:
                return False 
            self.balance *= self.int_rate + 1
            return self

Guido = User("Guido van Rossum", "guido@python.com", "")
Monty = User("Monty Python", "monty@python.com", "")


Guido.make_deposit(100)
Guido.make_deposit(200)
Monty.make_deposit(50)
Guido.make_withdrawal(50)
Monty.make_withdrawal(10)

print(Monty.account.balance)
Guido.display_user_balance()

Guido.transfer_money(Monty, 15)
print(Guido.account.balance)




