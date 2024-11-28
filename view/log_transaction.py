from datetime import datetime
import csv

def log_transaction(account_no, transaction_type, amount, new_balance):
    # Append transaction details to the transaction_history.csv file
    with open('transaction_history.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([datetime.now().strftime('%Y-%m-%d %H:%M:%S'), account_no, transaction_type, amount, new_balance])