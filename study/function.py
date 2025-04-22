account_Balance = 1000

def open_Account():
    print(f"현재 잔액은 {account_Balance}입니다")

def deposit(balance, money):
    print(f"입급이 완료되었습니다. 잔액은 {balance+money}입니다")
    return balance+money

def withdraw(balance, money):
    if(balance >= money):
        print(f"인출되었습니다. 잔액은 {balance-money}입니다.")
        return balance-money
    else:
        print(f"잔액이 부족합니다")

def withdraw_night(balance, money):
    commision = 100
    if (balance >= money+commision):
        print(f"인출되었습니다. 잔액은 {balance - money - commision}입니다.")
        return balance - money - commision
    else:
        print(f"잔액이 부족합니다")


open_Account()
account_Balance = deposit(account_Balance,500)
open_Account()
account_Balance = withdraw(account_Balance,200)
open_Account()
account_Balance = withdraw_night(account_Balance,500)
open_Account()