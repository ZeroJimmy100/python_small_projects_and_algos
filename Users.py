class User:
    def __init__(self, username, email, other_user):
        self.name = username			
        self.email = email		
        self.account_balance = 0       
        self.other_user = username
    def make_deposit(self, amount):	
    	self.account_balance += amount	
    def make_withdrawal(self, amount):
        self.account_balance -= amount
    def display_user_balance(self):
        BankBalance = {"User": self.name, "Balance": self.account_balance}
        print(BankBalance)
    def transfer_money(self, other_user, amount):
        self.account_balance -= amount
        other_user.account_balance += amount


Guido = User("Guido van Rossum", "guido@python.com", "")
Monty = User("Monty Python", "monty@python.com", "")


Guido.make_deposit(100)
Guido.make_deposit(200)
Monty.make_deposit(50)
Guido.make_withdrawal(50)
Monty.make_withdrawal(10)

print(Monty.account_balance)
Guido.display_user_balance()

Guido.transfer_money(Monty, 15)
print(Guido.account_balance)




