import datetime

threshold = 50000
balance = 0 


def user_transactions():
    user_data = {}
    print('Enter your transaction details. Enter "end" as Transaction ID to finish.')
    print('Enter "end" as User ID to stop adding users.')

    while True:
        user_id = input("User ID: ").strip()
        if user_id.lower() == "end":
            break
        
        print(f"Enter transactions for User ID: {user_id}.")
        transactions = []  
        
        while True:
            transaction_id = input("Transaction ID: ").strip()
            if transaction_id.lower() == "end":
                break

            try:
                transc_amount = float(input("Enter your transaction amount: "))
                location = input("Enter your location: ").strip()
                account_balance = float(input("Account Balance: "))
                time_str = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                
                transactions.append({"id": transaction_id,"transc_amount": transc_amount,"location": location,"time": time_str,"account_balance": account_balance})

            except ValueError:
                print("Invalid input. Please enter numeric values for amount and account balance.")

        user_data[user_id] = transactions  
    
    return user_data


def fraud_detect(transactions):
    suspicious_transactions = []
    for transaction in transactions:
        transc_amount = transaction["transc_amount"]
        account_balance = transaction["account_balance"]
        time_str = transaction["time"]
        time_obj = datetime.datetime.strptime(time_str, "%Y-%m-%d %H:%M:%S")

        if transc_amount > threshold:
            transaction["reason"] = "Amount exceeds threshold"
            suspicious_transactions.append(transaction)
        elif account_balance - transc_amount < balance:
            transaction["reason"] = "Insufficient account balance"
            suspicious_transactions.append(transaction)
        elif detect_time_oddity(time_obj):
            transaction["reason"] = "Transaction at unusual time"
            suspicious_transactions.append(transaction)
    
    return suspicious_transactions


def detect_time_oddity(transaction_time):
# Checks if a transaction occurs at an unusual time (e.g in between 12 am to 4 am)
    hour = transaction_time.hour
    return 0 <= hour <= 4


# _main_
print("Welcome to the Transaction Fraud Detection Application.")
user_data = user_transactions()

if not user_data:
    print("No transactions provided.")
else:
    for user_id, transactions in user_data.items():
        suspicious = fraud_detect(transactions)
        print(f"\nSuspicious Transactions for User ID: {user_id}:")
        if not suspicious:
            print("No suspicious transactions detected.")
        else:
            for transc in suspicious:
                print(f"Transaction ID: {transc['id']}, Amount: {transc['transc_amount']}, Location: {transc['location']}, Reason: {transc['reason']}")
