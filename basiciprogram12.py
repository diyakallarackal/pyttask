""""
Author=Diya Pradeep
Date=28-10-2024
Description=Write a program that simulates a simple bank ATM system.
"""
balance_amount=1000
while True:
    print("\n1,\t Check Balance")
    print("2,\t Deposit Money")
    print("3,\t Withdraw Money")
    print("4,\tExist")
    choice=int(input("Enter your choice:"))
    if choice==1:
        print(f"The current balance ${balance_amount}")
    elif choice==2:
        deposit_amount=float(input("Enter the amount:"))
        balance_amount+=deposit_amount
        print(f"The deposit amount ${deposit_amount} and " 
              f"the current balance${balance_amount}")
    elif choice==3:
        withdraw_amount = float(input("Enter the amount:"))
        if withdraw_amount>balance_amount:
            print("Insufficient amount")
        else:
            balance_amount -= withdraw_amount
            print(f"The withdraw amount${withdraw_amount} and "
                  f"the current balance${balance_amount}")
    elif choice ==4:
        break

    else:
        print("Invalid Entry")
