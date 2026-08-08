print("1. Deposit")
print("2. Withdraw")
print("3. Check balance")
print("4. Exit")

balance = 1000

while True:
    choice = int(input("choice:"))

    if choice == 1 :
        print("Deposit selected.")
        amount = int(input("How much do you want to deposit?"))
        balance = balance + amount
        print("Deposit successful!")
        print(f"Current balance: ${balance}")
    elif choice == 2:
        print("Withdraw selected.")
        withdraw_amount=int(input("how much do you want to withdraw?"))
        if balance >= withdraw_amount :
            balance = balance - withdraw_amount
            print("Withdraw successful!")
            print(f"Current balance: ${balance}")
        else:
            print("Insufficient balance!")
    elif choice == 3:
        print(f"Current balance: ${balance}")
    elif choice == 4:
        print("Goodbye.")
        break
    else:
        print("Invalid choice.")
