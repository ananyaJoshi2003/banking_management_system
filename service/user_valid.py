from colorama import init, Fore, Style

init()

class UserValid():    

    @staticmethod
    def check_name(name):

        try:
            if not name:
                raise ValueError("Name cannot be empty")
            
            if not name.replace(" ", "").isalpha():  # Allow spaces in name
                raise ValueError("Name should contain alphabets only")
            
            return True
        
        except ValueError as e:
            print(f"Name Error: {str(e)}")
            return False
        
        except Exception as e:
            print(f"Unexpected error while checking name: {str(e)}")
            return False

    @staticmethod
    def check_balance(balance_str):
        try:
            balance = float(balance_str)
            if balance < 500:
                print(f"{Fore.RED}Minimum initial balance should be ₹500{Style.RESET_ALL}")
                return False
            return True
        except ValueError:
            print(f"{Fore.RED}Please enter a valid number!{Style.RESET_ALL}")
            return False

    @staticmethod
    def check_mail(email):

        try:
            
            if not email:
                raise ValueError("Email cannot be empty")
                    
            if not email.endswith("@yash.com"):
                raise ValueError("Email must end with '@yash.com'")
                    
            return True

        except ValueError as e:
            print(f"Email Error: {str(e)}")
            return False

        except Exception as e:
            print(f"Unexpected error while checking email: {str(e)}")
            return False

    @staticmethod
    def check_password(password):
        try:

            if not password:
                raise ValueError("Password cannot be empty")
            
            if len(password) < 8:
                raise ValueError("Password must be at least 8 characters long")

            has_upper= False
            has_lower= False
            has_number= False
            special_chars= "!@#$%^&*()_+-=[]{}|;:,.<>?"
            has_special= False

            for char in password:

                if char.isupper():
                    has_upper = True

                elif char.islower():
                    has_lower = True

                elif char.isdigit():
                    has_number = True
                    
                elif char in special_chars:
                    has_special = True

            errors= []

            if not has_upper:
                errors.append("- At least 1 uppercase letter")

            if not has_lower:
                errors.append("- At least 1 lowercase letter")

            if not has_number:
                errors.append("- At least 1 number")
            
            if errors:
                print("\nPassword must contain:")
                for error in errors:
                    print(error)
                return False
            
            return True
        
        except ValueError as e:
            print(f"Password Error: {str(e)}")
            return False

        except Exception as e:
            print(f"Unexpected problem while checking password: {str(e)}")
            return False
