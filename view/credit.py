from colorama import Fore, Style, init
from model.db_methods import DbMethods
from service.retrive_account_details import get_accounts
from view.log_transaction import log_transaction
# from view.login import login_account

class Credit():

    def credit_money(self, account_no):
    
        print(f"{Fore.YELLOW}=== Credit Money ==={Style.RESET_ALL}")
        print(f"Your account number is: {account_no}")
        
        amount = input(f"{Fore.CYAN}How much money would you like to credit to your account? {Style.RESET_ALL}")

        if amount.replace('.', '', 1).isdigit() and float(amount) > 0:
            amount = float(amount)

            obj = DbMethods()
            obj.cr_amount(account_no, amount)
        else:
            print(f"{Fore.RED}Invalid input!{Style.RESET_ALL}")
