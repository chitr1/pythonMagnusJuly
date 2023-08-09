from abc import ABC,abstractmethod
class Accounts:
    def savings(self):
        print("No minimum balance and earn upto 7%monthly interest")

class Loans:
    def pl(self):
        print("Personal Loans")
       @abstractmethod
    def hl(self):
        print("Home Loans")
        @abstractmethod
obj1= Accounts()
obj1.savings()

class FinalAccount(Accounts,Loans):
    def pl(self):
        print("personal loan for 7% monthly")
    def hl(self):
        print("home loan for 10% monthly")

obj1=FinalAccount()
obj1.savings()
obj1.pl()


