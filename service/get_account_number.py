import csv

def get_last_account_number():
    try:
        with open('accounts.csv', 'r') as file:
            reader = csv.DictReader(file)
            accounts = list(reader)
            if accounts:  # If file is not empty
                return int(accounts[-1]['account_number'])  # Get the last account number
            return 11999  # Starting number if file is empty
    except FileNotFoundError:
        return 11999  # Starting number if file doesn't exist
    except Exception as e:
        print(f"Error reading account number: {str(e)}")
        return 11999
