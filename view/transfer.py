
# import csv

# class Transfer():

#     def transfer_money(from_account_no, to_account_no, amount):

#         accounts = []

#         with open('accounts.csv', mode='r') as file:

#             reader = csv.DictReader(file)

#             for row in reader:
#                 accounts.append(row)

#         from_account = next((acc for acc in accounts if acc['account_number']== from_account_no), None)
#         to_account = next((acc for acc in accounts if acc['account_number']== to_account_no), None)

#         if from_account is None or to_account is None:

#             print("One of the account numbers is invalid.")
#             return

#         if float(from_account['balance']) < amount:

#             print("Insufficient balance in the source account.")
#             return

#         from_account['balance'] = float(from_account['balance']) - amount
#         to_account['balance'] = float(to_account['balance']) + amount

#         with open('accounts.csv', mode='w', newline='') as file:

#             fieldnames = ['account_number', 'name', 'email', 'password', 'balance']
#             writer = csv.DictWriter(file, fieldnames=fieldnames)

#             writer.writeheader()
#             writer.writerows(accounts)

#         print(f"Successfully transferred {amount} from account {from_account_no} to account {to_account_no}.")
