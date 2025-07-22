class Bankaccount :
    Bank_name = "First National Bank"
def __init__(self, account_holder : str, initial_balance : float = 0.0):
    self.account_holder = account_holder
    self.balance = initial_balance
    self.transactions = []
def deposit(self, amount : float) -> None :
    if self.validate_amount(amount) :
        self.balance =+ amount
        self.transactions.append(f"Deposit :+{amount}$")
        print(f"{amount}$ deposited.New balance : {self.balance}$")
    else :
        print(f"Invalid deposit amount.")
def withdraw(self, amount :float) -> None :
    if self.validate_amount(amount) and amount <= self.balance :
        self.balance -= amount
        self.transactions.append(f"Withdrawal : -{amount}$")
        print(f"{amount}$ withdrawn.New balance : {self.balance}$ ")
    else:
        print(f"Invalid withdrawal amount.")

def __str__(self) ->str:
    return f"Account Holder : {self.account_holder}, Balance : {self.balance}$"

@classmethod
def Change_bank_name(cls, new_name : str) -> None :
    cls.bank_name = new_name
@staticmethod
def validate_amount(amount : float) -> bool:
    return amount > 0

#testing implementations
#Accounts_Transactions
Acc1 = Bankaccount("Alice", 1000)
Acc2 = Bankaccount("Bob",30)
Acc1.deposit(200)
Acc1.withdraw(1500)
Acc2.deposit(-50)
#printing accounts
print(Acc1)
print(Acc2)
#Validating amounts
print(f"Is -50 valid? {Bankaccount.validate_amount(-50)}")
#Changing Bank name
Bankaccount.change_bank_name("Citibank")

def show_transaction(self) -> None:
    if not self.transactions :
        print("no transactions detected.")
    else:
        print("transactions history :")
        for i in self.transactions:
            print(i)

class Savingsaccount(Bankaccount):
    def __init__(self, account_holder : str, initial_balance : float = 0.0, interest_rate : float = 0.01) :
        super().__init__(account_holder, initial_balance)
        self.interest_rate = interest_rate
    def add_interest(self) -> None :
        interest = self.balance * self.interest_rate
        self.deposit(interest)
    def __str__(self) ->str :
        interest_percent = self.interest_rate * 100
        return (f"Savingsaccount - Account Holder : {self.account_holder} ", f"Balance : {self.balance}$, Interest Rate : {interest_percent}%")
#testing savingsaccount
savings_acc = Savingsaccount("Charlie", 1000, 0.05) 
savings_acc.deposit(50)
savings_acc.add_interest()
print(savings_acc)
savings_acc.show_transactions()


