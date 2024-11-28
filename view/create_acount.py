import random
from colorama import init, Fore, Style
from model.db_methods import DbMethods
from service.user_valid import *
from service.save_account import *
from service.get_account_number import * 

init()

class create_account():

    
    def run(self):
        try:
            flag = True
            print(f"{Fore.CYAN}I am here to create your new account!!{Style.RESET_ALL}")
            
            while flag:
                name = input(f"{Fore.YELLOW}Enter your name:- {Style.RESET_ALL}")
                if(UserValid.check_name(name)):
                    break
            
            while flag:
                email = input(f"{Fore.YELLOW}Enter your email:- {Style.RESET_ALL}")
                if(UserValid.check_mail(email)):
                    break
                        
            while flag:
                password = input(f'''{Fore.YELLOW}Create password(should have at least 1 number, 1 uppercase, 1 lowercase): 
                {Style.RESET_ALL}''')
                if(UserValid.check_password(password)):
                    break

            while flag:
                initial_balance = input(f"{Fore.YELLOW}Enter initial balance (min ₹500):- {Style.RESET_ALL}")
                if(UserValid.check_balance(initial_balance)):
                    initial_balance = float(initial_balance)
                    break
            
            account_no = random.randint(1200, 10000)

            save = DbMethods()
            save.create_account(account_no, name, email, password, initial_balance)

        
        except Exception as e:
            print(f"{Fore.RED}Error creating account: {str(e)}{Style.RESET_ALL}")