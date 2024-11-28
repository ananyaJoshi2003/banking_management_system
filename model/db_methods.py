from colorama import Fore, Style
from model.db import DbConnection


class DbMethods():

    def __init__(self):
        
        con = DbConnection()
        self.connection, self.cursor = con.connection()

    def create_account(self, account_no, name, email, password, balance):

        try:

            query = '''insert into bank_db(account_no, name, email, password, balance) values(%s,%s,%s,%s,%s)'''
            self.cursor.execute(query, (account_no, name, email, password, balance))
            self.connection.commit()

            print(f"{Fore.GREEN}----------\nAccount created successfully!!\n----------{Style.RESET_ALL}")
            
            return True

        # except pymysql.MySQLError as e:
        #     print("ERROR:- unable to insert in table")

        except Exception:
            print("Gadbad ho gai")

    def login(self, email, password):

        try:

            query = '''SELECT * FROM bank_db WHERE email = %s AND password = %s'''
            self.cursor.execute(query, (email, password))

            user_data = self.cursor.fetchone()
            
            if user_data:
                print(f"{Fore.GREEN}----------\nLogin successful!\n----------{Style.RESET_ALL}")
                return user_data
            else:
                print(f"{Fore.RED}----------\nInvalid email or password!\n----------{Style.RESET_ALL}")
                return None

        except Exception as e:
            print(f"{Fore.RED}Error during login: {e}{Style.RESET_ALL}")

    def cr_amount(self, email, amount):

        try:

            get_balance_query = '''SELECT balance FROM bank_db WHERE email = %s'''
            self.cursor.execute(get_balance_query, (email,))
            current_balance = self.cursor.fetchone()

            if current_balance:

                new_balance = current_balance[0] + amount
                
                update_query = '''UPDATE bank_db SET balance = %s WHERE email = %s'''
                self.cursor.execute(update_query, (new_balance, email))
                self.connection.commit()

                print(f"{Fore.GREEN}----------\nAmount {amount} credited successfully!")
                print(f"Updated balance: {new_balance}\n----------{Style.RESET_ALL}")
                return True
            else:
                print(f"{Fore.RED}----------\nAccount not found!\n----------{Style.RESET_ALL}")
                return False

        except Exception as e:
            print(f"{Fore.RED}Error during credit: {e}{Style.RESET_ALL}")
            self.connection.rollback()
            return False

    def debit_money(self, email, amount):

        try:

            get_balance_query = '''SELECT balance FROM bank_db WHERE email = %s'''
            self.cursor.execute(get_balance_query, (email,))
            current_balance = self.cursor.fetchone()

            if current_balance:

                if current_balance[0] >= amount:

                    new_balance = current_balance[0] - amount
                    

                    update_query = '''UPDATE bank_db SET balance = %s WHERE email = %s'''
                    self.cursor.execute(update_query, (new_balance, email))
                    self.connection.commit()

                    print(f"{Fore.GREEN}----------\nAmount {amount} debited successfully!")
                    print(f"Updated balance: {new_balance}\n----------{Style.RESET_ALL}")
                    return True
                else:
                    print(f"{Fore.RED}----------\nInsufficient balance!")
                    print(f"Current balance: {current_balance[0]}")
                    print(f"Requested amount: {amount}\n----------{Style.RESET_ALL}")
                    return False
            else:
                print(f"{Fore.RED}----------\nAccount not found!\n----------{Style.RESET_ALL}")
                return False

        except Exception as e:
            print(f"{Fore.RED}Error during debit: {e}{Style.RESET_ALL}")
            self.connection.rollback() # undo changges agr error 
            return False

    def transfer(self, from_email, to_account_no, amount):

        try:
            get_balance_query = '''SELECT balance FROM bank_db WHERE email = %s'''
            self.cursor.execute(get_balance_query, (from_email,))
            sender_balance = self.cursor.fetchone()

            if not sender_balance:
                print(f"{Fore.RED}----------\nSender account not found!\n----------{Style.RESET_ALL}")
                return False

            if sender_balance[0] < amount:
                print(f"{Fore.RED}----------\nInsufficient balance!\nCurrent balance: {sender_balance[0]}\nRequired amount: {amount}\n----------{Style.RESET_ALL}")
                return False

            self.cursor.execute(get_balance_query, (to_account_no,))
            recipient_exists = self.cursor.fetchone()

            if not recipient_exists:
                print(f"{Fore.RED}----------\nRecipient account not found!\n----------{Style.RESET_ALL}")
                return False

            try:
                new_sender_balance = sender_balance[0] - amount
                update_query = '''UPDATE bank_db SET balance = %s WHERE email = %s'''
                self.cursor.execute(update_query, (new_sender_balance, from_email))

                if not self.cr_amount(to_account_no, amount):

                    self.connection.rollback()
                    print(f"{Fore.RED}----------\nTransfer failed! Transaction rolled back.\n----------{Style.RESET_ALL}")
                    return False

                self.connection.commit()
                print(f"{Fore.GREEN}----------\nTransfer successful!")
                print(f"Amount transferred: {amount}")
                print(f"Your updated balance: {new_sender_balance}\n----------{Style.RESET_ALL}")
                
                return True

            except Exception as e:
                self.connection.rollback()
                print(f"{Fore.RED}----------\nError during transfer: {e}")
                print("Transaction rolled back!\n----------{Style.RESET_ALL}")
                return False

        except Exception as e:
            print(f"{Fore.RED}----------\nError checking account details: {e}\n----------{Style.RESET_ALL}")
            return False
