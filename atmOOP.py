
import sys
class Atm:
    print("WELCOME TO NABIL BANK ATM !! ")
    def __init__(self):
        print("Please insert your Card.")
        self.pin = 1234
        self.balance = 15000
        self.menu()

    def menu(self):

        print("""
        What would you like to do !
        1. Balance Enquiry
        2. Withdraw Balance
        3. Deposit Balance
        4. Exit
        """)

        option = int(input("Chose any one option from 1-4: "))
        if option == 1:
            self.balance_inquiry()
            self.menu()

        elif option == 2:
            self.withdraw_balance()
            self.menu()

        elif option == 3:
            self.deposit_balance()
            self.menu()

        elif option == 4:
            print("THANKYOU FOR BANKING WITH US !!")
            sys.exit()

    def balance_inquiry(self):
        input_pin = int(input("Enter your pin number: "))
        if input_pin == self.pin:
         print("*" * 50)
         print(f"Your balance is {self.balance}")
         print("*" * 50)
        else:
            print("*" * 50)
            print("Incorrect pin!!")
            print(input("Please enter correct pin number: "))
            print("*" * 50)


    def withdraw_balance(self):
        input_pin = int(input("Enter your pin number: "))
        if input_pin == self.pin:
            print("*" * 50)

            withdraw_amt = int(input("Enter the amount to withdraw: "))
            if withdraw_amt <= self.balance:
                self.balance = self.balance - withdraw_amt
                print("*" * 50)
                print("Withdrawn Successfully!!")
                print("*" * 50)
                print(f"Your updated balance is {self.balance}.")
                print("*" * 50)
            else:
                print("You have insufficient balance !!")
        else:
            print("*" * 50)
            print("Incorrect pin!!")
            print(input("Please enter correct pin number: "))
            print("*" * 50)

    def deposit_balance(self):
        input_pin = int(input("Enter your pin number: "))
        if input_pin == self.pin:
            print("*"*50)
            deposit_amt = int(input("Enter the amount you want to deposit: "))
            self.balance = self.balance + deposit_amt
            print("*" * 50)
            print("Deposited Successfully!!")
            print("*" * 50)
            print(f"Your updated balance is {self.balance}.")
            print("*" * 50)
        else:
            print("*" * 50)
            print("Incorrect pin!!")
            print(input("Please enter correct pin number: "))
            print("*" * 50)
nabil : Atm()