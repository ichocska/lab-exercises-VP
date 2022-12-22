from entities.account import Account
from entities.bank import Bank
from entities.user import User
from entities.errors import *
class Menu():
    bank = Bank()
    def run(self):
        # infinite menu loopa
        while True:  
            self.PrintMenu()
            choice = int(input("Choose an item from the menu: \n> "))
            if choice == 7:
                break
            try:
                # process the user's choice
                if type(choice) == int and 6 >= choice > 0:    
                    self.MenuAction(choice)                
                else:
                    raise Exception("Error: Invalid choice")
            except Exception as ex:
                print(f"Error: {str(ex)}")
    def PrintMenu(self):
        print('==========MENU===============')
        print('Option 1: Create new User')
        print('Option 2: Create new Account for already Existing User')
        print('Option 3: Print all Users')
        print('Option 4: Print All User Accounts')
        print('Option 5: Deposit money into user account')
        print('Option 6: Withdraw money from user account')
        print('Option 7: Exit')
    def CreateUser(self):
        egn = input('Please enter user EGN')
        name = input('Please enter users names')
        user = User(egn, name)
        self.bank.users.append(user)
    def CreateAccount(self):
        egn = input('Please enter user EGN')
        for x in self.bank.users:
            if x.egn == egn:
                balance = float(input('Please enter balance'))
                currency = float(input('Please enter currency'))
                type = float(input('Please enter account type'))
                acc = Account(balance, currency, type)
                x.accounts.append(acc)
                return
            raise UserNotFound('The user was not found!')
    def PrintAllUsers(self):
        for x in self.bank.users:
            print(x)
    def PrintAllUserAccounts(self):
        egn = input('Please enter user EGN')
        for x in self.bank.users:
            if x.egn == egn:
                for y in x.accounts:
                    print(y)
            return
        raise UserNotFound('This user doesnt exist')
    def DepositMoneyIntoAccount(self):
        egn = input('Please enter user EGN')
        iban = input('Please enter user account IBAN')
        amount = float(input('Please enter amount of money you want to deposit'))
        for x in self.bank.users:
            if x.egn == egn:
                for y in x.accounts:
                    if y.IBAN == iban:
                        y.balance += amount
                        return
                    raise Exception('This account doesnt exist')
            return
        raise UserNotFound('This user doesnt exist')
    def WithdrawMoney(self):
        egn = input('Please enter user EGN')
        iban = input('Please enter user account IBAN')
        amount = float(input('Please enter amount of money you want to withdraw'))
        for x in self.bank.users:
            if x.egn == egn:
                for y in x.accounts:
                    if y.IBAN == iban:
                        if amount > y.balance:
                            raise InsufficientFunds('No money')
                        y.balance -= amount
    def MenuAction(self, commandNumber: int):
        match commandNumber:
            case 1:
                self.CreateUser()
            case 2:
                self.CreateAccount()
            case 3:
                self.PrintAllUsers()
            case 4:
                self.PrintAllUserAccounts()
            case 5:
                self.DepositMoneyIntoAccount()
            case 6:
                self.WithdrawMoney()

if __name__ == "__main__":
    menu = Menu()
    menu.run()