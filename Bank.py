def showBalance():
    print(f"\n** Your Balance is: {balance}$ **")


def deposit():
    print(f"\n** Your Balance is: {balance}$ **")
    try:
        amount = float(input("** Enter the amount to deposit: "))
        if amount > 0:
            return amount
        else:
            print("Enter a valid number!")
            deposit()
    except ValueError:
        print("Invalid input! Please enter a number.")
        deposit()


def withdraw():
    print(f"\n** Your Balance is: {balance}$ **")
    try:
        amount = float(input("** Enter the amount to withdraw: "))
        if amount <= balance and amount > 0:
            return amount
        else:
            print("You can't withdraw more than your balance!")
            withdraw()
    except ValueError:
        print("Invalid input! Please enter a number.")
        withdraw()


def main():
    balance = 0
    running = True

    while running:
        print("\n****** Banking Program ******")
        print("1. Check balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            showBalance()
        elif choice == "2":
            balance += deposit()
        elif choice == "3":
            balance -= withdraw()
        elif choice == "4":
            running = False
        else:
            print("Enter a valid choice.")


if __name__ == "__main__":
    main()
