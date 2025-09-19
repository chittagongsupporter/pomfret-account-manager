#!/usr/bin/env python3
# Simple CLI for account management
from accounts import view_accounts, add_account, remove_account

# Main CLI loop
def run_cli():
    while True:
        print("\nMenu:")
        print("1. View Accounts")
        print("2. Add Account")
        print("3. Remove Account")
        print("4. Exit")

        choice = input("Choose an option: ")

        # Handle user choices
        if choice == '1':
            view_accounts()
        elif choice == '2':
            account_name = input("Enter account name: ")
            result = add_account(account_name)
            print(result)
        elif choice == '3':
            account_name = input("Enter account name to remove: ")
            result = remove_account(account_name)
            print(result)
        elif choice == '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")
