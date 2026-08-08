def show_menu():
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check balance")
    print("4. Exit")

def deposit(balance):
    print("Deposit selected.")
    amount = int(input("How much do you want to deposit?"))
    balance = balance + amount
    print("Deposit successful!")
    print(f"Current balance: ${balance}")
    return balance

def withdraw(balance):
    print("Withdraw selected.")
    withdraw_amount=int(input("how much do you want to withdraw?"))
    if balance >= withdraw_amount :
        balance = balance - withdraw_amount
        print("Withdraw successful!")
        print(f"Current balance: ${balance}")
        return balance
    else:
        print("Insufficient balance!")
        return balance

def check_balance(balance):
    print(f"Current balance: ${balance}")

balance = 1000

while True:

    show_menu()

    choice = int(input("choice:"))

    if choice == 1:
        balance = deposit(balance)

    elif choice == 2:
        balance = withdraw(balance)

    elif choice == 3:
        check_balance(balance)

    elif choice == 4:
        print("goodbye")
        break

    else:
        print("Invalid choice.")
        
    
