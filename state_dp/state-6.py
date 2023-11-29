from abc import ABCMeta

class IState(metaclass=ABCMeta):
    
    def getBenefits(self):
        pass
    
class GoldState(IState):
    
    def getBenefits(self):
        print("---------------------------------------------")
        print("Account is in Gold State.Your Benefits are listed below:")
        print("15% off on groceries")
        print("20% off on beauty products")
        print("---------------------------------------------")

class PlatinumState(IState):
    
    def getBenefits(self):
        print("---------------------------------------------")
        print("Account is in Platinum State.Your Benefits are listed below:")
        print("20% off on groceries")
        print("25% off on beauty products")
        print("---------------------------------------------")
        
class SliverState(IState):
    
    def getBenefits(self):
        print("---------------------------------------------")
        print("Account is in Sliver State.Your Benefits are listed below:")
        print("10% off on groceries")
        print("15% off on beauty products")
        print("---------------------------------------------")
        
        
class Account:
    
    def __init__(self):
        self.state = SliverState()
        self.balance = 0
        
    def deposit(self, amount):
        self.balance += amount
        
    def withdraw(self, amount):
        self.balance -= amount
        
    def getCurrentBenefits(self):
        self.state.getBenefits()
        
    def evaluateState(self):
        if self.balance <= 5000:
            self.state = SliverState()
        elif self.balance > 5000 and self.balance < 10000:
            self.state = GoldState()
        elif self.balance >= 10000:
            self.state = PlatinumState()
            
if __name__ == "__main__":
    account = Account()
    account.deposit(amount=1000)
    account.getCurrentBenefits()
    
    account.deposit(amount=10000)
    account.getCurrentBenefits()
    
    account.withdraw(amount=4000)
    account.getCurrentBenefits()