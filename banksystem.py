class bankofvijay():
    def __init__(self,holder_name,account_number,initial_balance=0,accoun_type="saving"):
        self.holder = holder_name
        self.accnum = account_number
        self.accbal = initial_balance
        self.accty = accoun_type
    def deposit(self,amount):
        if amount != 0:
            self.accbal += amount
        else:
            print("paisanhi jai na")
    def widrawl(self,amount):
        if amount > self.accbal:
            print("insufficiant bal")
        elif amount != 0:
            self.accbal -= amount
        else:
            print("enter valid response")
    def accountin(self):
        return f"the holder:{self.holder} | the acc number : {self.accnum} | acc balance {self.accbal} | type of acc {self.accty}"
    def interest(self):
        if "saving" in {self.accty}:
            print(self.accbal * 0.05)
        else:
            print("only for savings")

acc1=bankofvijay("yash",676767,1000)
acc1.deposit(140)
acc1.widrawl(500)
print(acc1.interest())
print(acc1.accountin())