from colorama import Fore, Back, Style, init
from service.retrive_account_details import *
from view.create_acount import create_account
from view.login import login_account
from constant.constant import *
# from view.credit import credit_money

init(autoreset=True)

class BankController:
    # def __init__(self):
    
    def run(self):
        print(f"{Fore.CYAN}-------------------")
        print(f"{Fore.YELLOW}Welcome to our banking management system")
        print(f"{Fore.CYAN}-------------------{Style.RESET_ALL}")

        while True:
            print(f"\n{Fore.GREEN}Menu Options:")
            menu = f"""Choose an option:- 
{Fore.CYAN}1) Create New Account
{Fore.CYAN}2) Login 
{Fore.RED}3) Exit {Style.RESET_ALL}
"""
            chose = int(input(menu))

            if chose == SIGNUP:
                print(f"{Fore.YELLOW}=== Create New Account ==={Style.RESET_ALL}")
                create = create_account()
                create.run()

            elif chose == LOGIN:
                print(f"{Fore.YELLOW}=== Login ==={Style.RESET_ALL}")
                login = login_account()
                login.run()

            elif chose == EXIT:
                print(f"{Fore.YELLOW}THANK YOU")
                print(f"{Fore.GREEN}Visit Again!{Style.RESET_ALL}")
                break

            else:
                print(f"{Fore.RED}Invalid option! Please choose a correct option (1-4){Style.RESET_ALL}")
