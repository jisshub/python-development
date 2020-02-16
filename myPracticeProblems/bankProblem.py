class MyBank:
    initialBal = 5000
    holderacc = None
    holdername = None

    def __init__(self, hello):
        self.hello = hello

        print("1. Add Account" '\n' "2. deposit cash" '\n' "3. withdraw cash"
              '\n'"4. Bank Statement" '\n' "5. Exit")

        def options(i):
            if i == 1:
                print(self.addAccount())
                # call init function again
                self.__init__()
            elif i == 2:
                print(self.cashDeposit())
                self.__init__()
            elif i == 3:
                print(self.withdrawCash())
                self.__init__()
            elif i == 4:
                print(self.bankStatement())
                self.__init__()
            elif i == 5:
                return "Thanks for Banking"
            else:
                print("Wrong Choice")
                self.__init__()

        i = int(input("Enter option: "))
        print(options(i))



    def addAccount(self):
        self.holdername = input("Enter Name: ")
        self.holderacc = input("Enter Acc no: ")
        return f"name: {self.holdername}, accoun no:{self.holderacc},balance: {self.initialBal})"

    def cashDeposit(self):
        depAmount = int(input("Amount to Deposit: "))
        self.initialBal += depAmount
        return f"your new balance: {self.initialBal}"

    def withdrawCash(self):
        withDrawAmount = int(input("Amount to Withdraw: "))
        self.initialBal -= withDrawAmount
        return f"your new balance: {self.initialBal}"

    def bankStatement(self):
        return f"Name:{self.holdername} \n Account no: {self.holderacc}" \
               f"\n Balance: {self.initialBal}"



b = MyBank()
