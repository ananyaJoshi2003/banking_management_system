from colorama import init, Fore, Style

import csv

def get_accounts():
    csv_file = 'accounts.csv'
    accounts = []

    try:
        with open(csv_file, 'r', newline='') as file:
            reader = csv.DictReader(file)
            accounts = list(reader)
    except FileNotFoundError:
        print(f"{Fore.RED}accounts.csv file not found.{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}Error reading accounts: {str(e)}{Style.RESET_ALL}")
    
    return accounts
