from colorama import Fore, Back, Style, init
from model.db_methods import DbMethods
from service.retrive_account_details import *
from datetime import datetime
# from view.log_transaction import log_transaction

class Debit():

    def debit_money(self, account_no):       
    
        print(f"{Fore.YELLOW}=== Debit Money ==={Style.RESET_ALL}")
        print(f"Your account number is: {account_no}")

        amount = input(f"{Fore.CYAN}How much money would you like to debit from your account? {Style.RESET_ALL}")

        if amount.replace('.', '', 1).isdigit() and float(amount) > 0:
            amount = float(amount)

            debit = DbMethods()
            debit.debit_money(account_no, amount)
        else:
            print(f"{Fore.RED}Invalid input!{Style.RESET_ALL}")


        #     accounts = get_accounts()
        #     account_found = False

        #     for account in accounts:
        #         if account['account_number'] == account_no:
        #             account_found = True
        #             current_balance = float(account['balance'])

        #             if current_balance >= amount:
        #                 new_balance = current_balance - amount
        #                 account['balance'] = new_balance  
        #                 print(f"{Fore.GREEN}Successfully debited {amount} from your account! New balance: {new_balance}{Style.RESET_ALL}")

        #                 # Log the transaction
        #                 log_transaction(account_no, 'debit', amount, new_balance)

        #             else:
        #                 print(f"{Fore.RED}Insufficient balance! You cannot debit {amount} from your account.{Style.RESET_ALL}")

        #             break

        #     if account_found:
        #         with open('accounts.csv', 'w', newline='') as file:
        #             fieldnames = ['account_number', 'name', 'email', 'password', 'balance']
        #             writer = csv.DictWriter(file, fieldnames=fieldnames)
        #             writer.writeheader()
        #             writer.writerows(accounts)
        #     else:
        #         print(f"{Fore.RED}Account not found.{Style.RESET_ALL}")

        # else:
        #     print(f"{Fore.RED}Invalid input! Please enter a valid amount greater than zero.{Style.RESET_ALL}")

