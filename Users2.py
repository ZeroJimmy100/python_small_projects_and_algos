class User:
    def __init__(self, username, email, other_user):
        self.name = username			
        self.email = email		
        self.account_balance = 0       
        self.other_user = username
    def make_deposit(self, amount):	
        self.account_balance += amount	
        return self
    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self
    def display_user_balance(self):
        BankBalance = {"User": self.name, "Balance": self.account_balance}
        print(BankBalance)
        return self
        
    def transfer_money(self, other_user, amount):
        self.account_balance -= amount
        other_user.account_balance += amount
        
        


Guido = User("Guido van Rossum", "guido@python.com", "")
Monty = User("Monty Python", "monty@python.com", "")


Guido.make_deposit(100).make_deposit(200).make_deposit(300).make_withdrawal(50).display_user_balance()







