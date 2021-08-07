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
		
    
Michael = BankAccount(2, 100)
Brandon = BankAccount(2, 300)

Michael.deposit(200).withdraw(150).yield_interest().display_account_info()



    