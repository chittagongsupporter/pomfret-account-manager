# Simple account management system
accounts = []

# View all accounts
def view_accounts():
    if accounts:
        for account in accounts:
            print("Account: " + account)
    else:
        print("No accounts available.")

# Add a new account with validation
def add_account(account_name):
    if not account_name:
        return "Account name cannot be empty."
    elif account_name in accounts:
        return "Account already exists."
    elif len(account_name) < 3:
        return "Account name must be at least 3 characters long."
    elif len(account_name) > 20:
        return "Account name must be less than 20 characters long."
    elif not account_name.isalnum():
        return "Account name must be alphanumeric."
    elif ' ' in account_name:
        return "Account name cannot contain spaces."
    elif any(char in account_name for char in "!@#$%^&*()[]{};:,./<>?\\|`~-=_+"):
        return "Account name cannot contain special characters."
    else:
        accounts.append(account_name)
        return f"Account '{account_name}' added successfully."

# Remove an account
def remove_account(account_name):
    if account_name in accounts:
        accounts.remove(account_name)
        return f"Account '{account_name}' removed successfully."
    else:
        return f"Account '{account_name}' not found."
