import sys

#account balance 
account_balance = float(500.25)


# Defining custom functions to be used in script. The outputs are built into these functions.
# This is so that when it is called upon, all of the work has been done. 
def printBalance():
  print(account_balance)

def deposit(amount):
  print("Deposit was $%.2f, current balance is $%.2f" %(amount, account_balance + amount))

def withdraw(amount):
  if amount > account_balance: 
    print("$%.2f is greater than your account balance of $%.2f" %(withdrawalAmount, account_balance))
  else:
    print("Withdrawal amount was $%.2f, current balance is $%.2f" %(amount, account_balance - amount)) 

def printSummary():
  print("Thank you for banking with us.")
  

#User input(parameters) to be used in the custom functions.

userchoice = input ("What would you like to do?\n")

if (userchoice == 'D'):
  depositAmount = (int(float(input('How much would you like to deposit today? \n'))))  
  deposit(depositAmount)
elif (userchoice == 'W'):
  withdrawalAmount = int(float(input("How much would you like to withdraw today? \n")))
  withdraw(withdrawalAmount)
elif (userchoice == 'B'):
  print('Your current balance: ' + str(printBalance(account_balance)))
else:
  printSummary()