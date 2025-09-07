balance = 0
isRuning = True

def showBalance():
    print(f"Your balance is ${balance:.2f}")

def deposit():
    amount = float(input("Enter an amount to be deposited: "))
    if amount < 0:
        print("That is nit a valid amount")
    else:
        return amount

def withdraw():
    amount = float(input("Enter an amount to be withdrawed: "))
    if amount > balance:
        print("Insufficient funds")
    else:
        if amount < 0:
            print("Amount must be greater than zero")
        else:
            return amount
while isRuning:
    print("Banking Program")
    print("1. Show Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = input("Enter your choice(1-4): ")

    if choice == "1":
        showBalance()
    elif choice == "2":
        balance += deposit()
    elif choice == "3":
        balance -= withdraw()
    elif choice == "4":
        isRuning = False
    else:
        print("That is not a valid choice")



print("Thank you have a nice day!")