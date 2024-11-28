from colorama import Fore, Style
import maskpass
from constant.login_constamt import *
from model.db_methods import DbMethods
from view.credit import Credit
from view.debit import Debit
from view.transection import Transaction
# from view.transfer import Transfer, transfer_money
# from view.transfer import transfer_money

class login_account():
    def run(self):
        user_id = input("Enter your id (mail id): ")
        password=maskpass.askpass(Fore.MAGENTA +"Enter your password: "+Style.RESET_ALL,mask="*") 

        obj = DbMethods()
        user_data = obj.login(user_id, password)

        if user_data:
            try:
                while True:
                    print(f"\n{Fore.GREEN}Menu options:")
                    menu = f"""Choose an option:- 
                    {Fore.CYAN}1) Credit Money
                    {Fore.CYAN}2) Debit Money 
                    {Fore.CYAN}3) Transaction history 
                    {Fore.CYAN}4) Transfer money
                    {Fore.RED}5) Exit {Style.RESET_ALL}
                    """
                    chose = int(input(menu))

                    # account_no = user_data[0]  

                    if chose == CREDIT:
                        print(f"{Fore.YELLOW}=== Credit Money ==={Style.RESET_ALL}")
                        credit = Credit()
                        credit.credit_money(user_id)

                    elif chose == DEBIT:
                        print(f"{Fore.YELLOW}=== Debit Money ==={Style.RESET_ALL}")
                        debit = Debit()
                        debit.debit_money(user_id)

                    elif chose == HISTORY:
                        print(f"{Fore.YELLOW}=== Transaction History ==={Style.RESET_ALL}")
                        transaction = Transaction()
                        transaction.view_last_transactions(user_id)

                    elif chose == TRANSFER:
                        print(f"{Fore.YELLOW}=== Transfer Money ==={Style.RESET_ALL}")
                        to_account_no = input("Enter the account number to transfer to: ")
                        amount = float(input("Enter the amount to transfer: "))

                        obj.transfer(user_id, to_account_no, amount)
                        

                    elif chose == EXIT:
                        print(f"{Fore.YELLOW}THANK YOU{Style.RESET_ALL}")
                        break

                    else:
                        print(f"{Fore.RED}Invalid option! Please choose a correct option (1-5){Style.RESET_ALL}")

            except ValueError:
                print(f"{Fore.RED}Please enter a valid number for menu choice!{Style.RESET_ALL}")
            except Exception as e:
                print(f"{Fore.RED}An error occurred: {e}{Style.RESET_ALL}")