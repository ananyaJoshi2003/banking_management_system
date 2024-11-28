import csv
# import os
# from datetime import datetime
from colorama import init, Fore, Style
# from service.retrive_account_details import get_accounts

class Transaction():
    
    def view_last_transactions(self, account_no):

        try:

            with open('transaction_history.csv', 'r') as file:

                reader = csv.reader(file)
                print(f"{Fore.YELLOW}=== Transaction History for Account Number: {account_no} ==={Style.RESET_ALL}")
                found = False

                for row in reader:

                    if row[1] == account_no:

                        found = True
                        print(f"Date: {row[0]}, Type: {row[2]}, Amount: {row[3]}, New Balance: {row[4]}")

                if not found:
                    print(f"{Fore.RED}No transactions found for this account.{Style.RESET_ALL}")
                    
        except FileNotFoundError:
            print(f"{Fore.RED}Transaction history file not found.{Style.RESET_ALL}")
