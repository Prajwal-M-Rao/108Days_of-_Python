from datetime import datetime

# Initial ATM setup
actual_pin = None  # Stores the user's PIN
inserted = False  # Tracks whether the card is inserted
balance = 1000  # Initial balance
transactions = []  # Stores transactions
exit_program = False  # Tracks program exit status

while not exit_program:  # Ensures complete exit when user selects option 5
    print("\nWelcome to SBI ATM")

    if not inserted:
        try:
            a = int(input("Insert ATM Card\n 1. Yes\n 2. No\n"))
        except ValueError:
            print("Invalid input! Please enter 1 or 2.")
            continue

        if a == 1:
            inserted = True  # Card inserted

            # Set PIN if it's not already set
            if not actual_pin:
                actual_pin = input("Set a new PIN: ")

            # PIN Verification
            pin = input("Enter your PIN: ")
            if pin == actual_pin:
                while True:
                    print('''
                    1. Deposit
                    2. Withdraw
                    3. Mini statement
                    4. PIN Change
                    5. Exit
                    ''')

                    try:
                        option = int(input("Choose an option: "))
                    except ValueError:
                        print("Invalid input! Please enter a number between 1 and 5.")
                        continue

                    # Deposit money
                    if option == 1:
                        try:
                            amount = int(input("Enter deposit amount: "))
                            if amount > 0:
                                balance += amount
                                transactions.append(f"Deposited: +₹{amount}")
                                print("Cash has been deposited successfully.")
                            else:
                                print("Enter a valid deposit amount.")
                        except ValueError:
                            print("Invalid input! Please enter a numeric value.")

                    # Withdraw money
                    elif option == 2:
                        try:
                            amount = int(input("Enter withdrawal amount: "))
                            if amount <= 0:
                                print("Enter a valid amount.")
                            elif amount % 100 != 0:
                                print("Please enter an amount in multiples of ₹100.")
                            elif amount > balance:
                                print("Insufficient balance.")
                            else:
                                balance -= amount
                                transactions.append(f"Withdrawn: -₹{amount}")
                                print("Take your cash.")
                        except ValueError:
                            print("Invalid input! Please enter a numeric value.")

                    # Mini statement
                    elif option == 3:
                        datime = datetime.now()
                        date = datime.strftime("%d-%m-%Y")
                        time = datime.strftime("%I:%M %p")
                        print(f'''
                        State Bank of India
                        Date: {date}     Time: {time}

                        Transactions:
                        ''')
                        if transactions:
                            for transaction in transactions:
                                print(transaction)
                        else:
                            print("No transactions yet.")
                        print("Available Balance: ₹", balance)

                    # Change PIN
                    elif option == 4:
                        new_pin = input("Enter new PIN: ")
                        actual_pin = new_pin
                        print("PIN successfully changed.")

                    # Exit program
                    elif option == 5:
                        print("Thank you for using SBI ATM.")
                        exit_program = True  # Set exit flag to True
                        break  # Exit the inner loop

                    else:
                        print("Invalid option, please choose between 1 and 5.")

            else:
                print("Incorrect PIN. Try again.")

        elif a == 2:
            print("Please insert your ATM card to continue.")
        else:
            print("Invalid option. Please enter 1 or 2.")
