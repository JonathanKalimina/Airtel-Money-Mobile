# Airtel Money Mobile Simulation

accounts = []
transactions = []


# Create an account
def create_account():
    print("\n========== CREATE ACCOUNT ==========")

    phone_number = input("Enter phone number: ")
    password = input("Enter password: ")

    # Check if the phone number already exists
    for account in accounts:
        if account[0] == phone_number:
            print("An account with this phone number already exists.")
            return

    # [phone number, password, balance]
    new_account = [phone_number, password, 0]

    accounts.append(new_account)

    print("Account created successfully!")


# Login
def login():
    print("\n========== LOGIN ==========")

    phone_number = input("Enter phone number: ")
    password = input("Enter password: ")

    for account in accounts:
        if account[0] == phone_number and account[1] == password:
            print("Login successful!")
            return account

    print("Invalid phone number or password.")
    return None


# View balance
def view_balance(account):
    print(f"\nYour balance is K{account[2]:.2f}")


# Deposit money
def deposit_money(account):
    amount = float(input("Enter amount to deposit: K"))

    if amount <= 0:
        print("Invalid amount.")

    else:
        account[2] = account[2] + amount

        print(f"K{amount:.2f} deposited successfully.")
        print(f"Your new balance is K{account[2]:.2f}")


# Send money
def send_money(account):
    recipient_number = input("Enter recipient phone number: ")
    amount = float(input("Enter amount to send: K"))

    if amount <= 0:
        print("Invalid amount.")
        return

    if amount > account[2]:
        print("Insufficient balance.")
        return

    # Find recipient
    for recipient in accounts:

        if recipient[0] == recipient_number:

            # Prevent sending money to yourself
            if recipient is account:
                print("You cannot send money to yourself.")
                return

            # Remove money from sender
            account[2] = account[2] - amount

            # Add money to recipient
            recipient[2] = recipient[2] + amount

            # Store the transaction
            # [sender, recipient, amount]
            transactions.append([account, recipient, amount])

            print(f"K{amount:.2f} sent successfully to {recipient_number}.")
            print(f"Your new balance is K{account[2]:.2f}")

            return

    print("Recipient phone number not registered with Airtel Money Mobile.")


# Reverse the user's last transaction
def reverse_transaction(account):

    # Search backwards through transactions
    for i in range(len(transactions) - 1, -1, -1):

        transaction = transactions[i]

        sender = transaction[0]
        recipient = transaction[1]
        amount = transaction[2]

        # Make sure this transaction belongs to the logged-in user
        if sender is account:
            # Return money to the sender
            sender[2] = sender[2] + amount

            # Remove money from the recipient
            recipient[2] = recipient[2] - amount

            # Remove the transaction from the list
            transactions.pop(i)

            print("\nTransaction reversed successfully.")
            print(f"K{amount:.2f} has been returned to your account.")
            print(f"Your new balance is K{sender[2]:.2f}")

            return

    print("\nYou have no transaction to reverse.")


# Change password
def change_password(account):
    old_password = input("Enter current password: ")

    if old_password == account[1]:

        new_password = input("Enter new password: ")

        account[1] = new_password

        print("Password changed successfully.")

    else:
        print("Incorrect current password.")


# Main menu
def main_menu(account):

    while True:

        print("\n========= AIRTEL MONEY =========")
        print("1. View Balance")
        print("2. Send Money")
        print("3. Deposit Money")
        print("4. Reverse Last Transaction")
        print("5. Change Password")
        print("6. Logout")

        choice = input("Choose an option: ")

        if choice == "1":
            view_balance(account)

        elif choice == "2":
            send_money(account)

        elif choice == "3":
            deposit_money(account)

        elif choice == "4":
            reverse_transaction(account)

        elif choice == "5":
            change_password(account)

        elif choice == "6":
            print("You have logged out.")
            break

        else:
            print("Invalid choice. Please try again.")


# Main program
while True:

    print("\n========== AIRTEL MONEY MOBILE ==========")
    print("1. Create an Account")
    print("2. Login")
    print("3. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        create_account()

    elif choice == "2":

        logged_in_account = login()

        if logged_in_account is not None:
            main_menu(logged_in_account)

    elif choice == "3":
        print("Thank you for using Airtel Money.")
        break

    else:
        print("Invalid choice. Please try again.")