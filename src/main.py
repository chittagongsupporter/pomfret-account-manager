accounts = []
def main():
    while True:
        print("\nMenu:")
        print("1. View Accounts")
        print("2. Add Account")
        print("3. Remove Account")
        print("4. Exit")

        choice = input("Choose an option: ")
        
        if choice == '1':
            viewAccounts()
        elif choice == '2':
            addAccount()
        elif choice == '3':
            removeAccount()
        elif choice == '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")


def viewAccounts():
    print("\nAccounts:")

    if accounts:
        for account in accounts:
            print("Account: " + account)
    else:
        print("No accounts available.")
        print("Please add an account.")
        addAccount()

def addAccount():
    while True:
        account_name = input("Enter account name: ")

        if not account_name:
            print("Account name cannot be empty. Please try again.")
            continue
        elif account_name in accounts:
            print("Account already exists. Please try again.")
            continue
        elif len(account_name) < 3:
            print("Account name must be at least 3 characters long. Please try again.")
            continue
        elif len(account_name) > 20:
            print("Account name must be less than 20 characters long. Please try again.")
            continue
        elif not account_name.isalnum():
            print("Account name must be alphanumeric. Please try again.")
            continue
        elif ' ' in account_name:
            print("Account name cannot contain spaces. Please try again.")
            continue
        elif any(char in account_name for char in "!@#$%^&*()[]{};:,./<>?\|`~-=_+"):
            print("Account name cannot contain special characters. Please try again.")
            continue
        else:
            break

    accounts.append(account_name)
    print(f"Account '{account_name}' added successfully.")
    viewAccounts()

def removeAccount():
    account_name = input("Enter account name to remove: ")

    if account_name in accounts:
        accounts.remove(account_name)
        print(f"Account '{account_name}' removed successfully.")
    else:
        print(f"Account '{account_name}' not found.")

    viewAccounts()

main()

