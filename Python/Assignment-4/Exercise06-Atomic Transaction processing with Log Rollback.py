"""
Scenario
A bank updates user balances in a database dictionary based on transaction files. To ensure accounting
consistency, if any single transaction in a batch contains an error (such as a negative transfer amount, an
unrecognized account number, or an overdraft), the entire batch must fail, all accounts must be restored
to their initial states, and a rollback action must be logged to a text file.

Problem Description
1. Define three custom exception classes inheriting from Exception:
AccountNotFoundError (raised when an account ID is missing from the registry).
OverdraftError (raised when a withdrawal amount exceeds the account balance).
InvalidTransactionError (raised when the transaction type is unrecognized or if
transaction amounts are non-positive).

2. Write a function process_transaction_batch(accounts, batch_list, log_path):
accounts is a dictionary where keys are account numbers (strings) and values are balances
(floats), e.g., {"ACC01": 500.0, "ACC02": 200.0}.
batch_list is a list of dictionaries representing transactions, e.g.:
[
    {"acc": "ACC01", "type": "deposit", "amt": 150.0},
    {"acc": "ACC02", "type": "withdraw", "amt": 50.0}
]
log_path is a string referencing the path of the transaction log file.

Atomicity Requirements:
Create a deep copy of the accounts dictionary before starting any transaction
modifications to act as a restore point (backup).

Iterate through batch_list and apply the changes to accounts:
- If the transaction "acc" does not exist in accounts, raise
AccountNotFoundError with message: "Account '<acc>' not found."
- If transaction "type" is not "deposit" or "withdraw", raise
InvalidTransactionError with message: "Invalid transaction type '<type>'."
- If transaction "amt" is less than or equal to 0, raise
InvalidTransactionError with message: "Transaction amount must be positive."
- If transaction "type" is "withdraw" and the account balance is less than
"amt", raise OverdraftError with message: "Insufficient funds. Account <acc> has balance <bal>, requested <amt>."

Exception Handling & Rollback:
If any exception is raised during the processing of the list, catch the exception:
- Restore the accounts dictionary to the exact state saved in your backup.
- Open the file at log_path (create it if it doesn't exist, append to it if it does) and write the following entry: 
  [ROLLBACK] Batch aborted: <Exception Class Name> - <Exception Message>\n
- Re-raise the caught exception so that the calling program knows the transaction batch failed.

If all transactions in the batch are executed successfully:
- Open the file at log_path and write: 
  [SUCCESS] Batch completed. <number_of_transactions> transaction(s) processed.\n
- Return the updated accounts dictionary.

Constraint: Ensure all file operations are safely cleaned up. Use context managers (with open(...)) or try...finally to write to the log file.

Example Walkthrough
accounts = {"ACC01": 100.0, "ACC02": 50.0}
log_file = "transactions.log"

# Batch 1: Valid transactions
batch_1 = [
    {"acc": "ACC01", "type": "withdraw", "amt": 30.0},
    {"acc": "ACC02", "type": "deposit", "amt": 20.0}
]
accounts = process_transaction_batch(accounts, batch_1, log_file)
# Result: accounts changes to {"ACC01": 70.0, "ACC02": 70.0}
# transactions.log writes: "[SUCCESS] Batch completed. 2 transaction(s) processed."

# Batch 2: Invalid transaction (triggers rollback)
batch_2 = [
    {"acc": "ACC01", "type": "deposit", "amt": 50.0},
    {"acc": "ACC02", "type": "withdraw", "amt": 200.0} # Overdraft!
]
try:
    accounts = process_transaction_batch(accounts, batch_2, log_file)
except OverdraftError as e:
    print(f"Caught: {e}")
# Verify Rollback: ACC01 must remain 70.0, NOT updated to 120.0.
print(accounts) # Output: {"ACC01": 70.0, "ACC02": 70.0}
# transactions.log writes: "[ROLLBACK] Batch aborted: OverdraftError - Insufficient funds. Account ACC02 has balance 70.0, requested 200.0."
"""
# Importing Required Libraries
from pprint import pprint
import copy


# Creating Custom Exceptions
class AccountNotFoundError(Exception):
    pass

class InvalidTransactionError(Exception):
    pass

class OverdraftError(Exception):
    pass

def line():
    pprint("_"*90)
    return()

# This Function calls the main function and catches error  if occured 
def Try_Except(accounts,batch_list,log_file):
    try:
        accounts=process_transaction_batch(accounts, batch_list,log_file)
        print(f"{accounts=}")
    except OverdraftError as OE:
        print(f"Caught OverdraftError: {OE}")
    except InvalidTransactionError as ITE:
        print(f"Caught InvalidTransactionError: {ITE}")
    except AccountNotFoundError as ANF:
        print(f"Caught AccountNotFoundError: {ANF}")


# This is main function which processes all data
def process_transaction_batch(accounts, batch_list,log_file):

    # Taking Copy of Current state of Accounts, can be used in case of rollback
    count=0 # count for successfull transactions
    backup=copy.deepcopy(accounts)

    # Iterating in batch list  
    for transactions in batch_list:

        #finding if accounts on whcih transaction are going to perform do exist in accounts or not 
        current_acc=transactions["acc"]
        if(transactions["acc"] not in accounts.keys()):
            accounts=backup # Rollback
            print(f"ROLLBACK {accounts=}")

            # Updating Log File
            with open(log_file,mode="w") as  T:
                T.write(f"[RollBack] AccountNotFoundError: Account with id {transactions["acc"]} Not Found")
            raise AccountNotFoundError(f"Account {current_acc} not found.") # custom error raised

        # finding if accounts on which transaction are going to perform has type withdraw or deposit only 
        if(transactions["type"].strip().lower() not in ("withdraw","deposit")):
            accounts=backup # Rollback
            print(f"ROLLBACK {accounts=}")

            # Updating Log File
            with open(log_file,mode="w") as T:
                T.write(f"RollBack] InvalidTransactionError has Occured at {transactions["type"]}!")
            raise InvalidTransactionError("Transaction Type Must be Deposit or Withdraw only!")

        # if Transaction type=Deposit
        if(transactions["type"].strip().lower()=="deposit"):
            try:
                # Adding Deposited Value
                accounts[current_acc]=accounts[current_acc]+transactions["amt"]
                count+=1    # Successfull Transaction Count Increased by 1

                # Updating Log File
                with open(log_file,mode="w") as T:
                    T.write(f" [SUCCESS] . {count} transaction(s) processed.")
                print(f"Balance of acc: {current_acc} has become {accounts[current_acc]} from {((accounts[current_acc])-transactions["amt"])}")

            except:

                accounts=backup # Rollback
                print(f"{accounts=}")
                line()
                print("Something Went Wrong")
                return()
            
        # elif Transaction type=withdraw
        elif(transactions["type"].strip().lower()=="withdraw"):

            # Checking if account has enough balace to withdraw
            if(transactions["amt"]>accounts[current_acc]):
                accounts=backup # Rollback
                print(f"ROLLBACK: {accounts=}")

                # Updating Log File
                with open(log_file,mode="w") as T:
                    T.write(f'[ROLLBACK] Batch aborted: OverDraft -Insufficient funds. Account {transactions["acc"]} has balance {accounts[current_acc]}, requested {transactions["amt"]}')
                raise OverdraftError(f"Insufficient funds. Account {current_acc} has balance {accounts[current_acc]}, requested {transactions["amt"]}")

            # Withdrawing action
            try:
                # Removal of Ammount from acc
                accounts[current_acc]=accounts[current_acc]-(transactions["amt"])
                count+=1

                # Updating Log File
                with open(log_file,mode="w") as T:
                    T.write(f" [SUCCESS] . {count} transactions processed.")
                print(f"Balance of acc: {transactions["acc"]} has become {accounts[current_acc]} from {accounts[current_acc]+transactions["amt"]}")
        
            
    
            except:
                accounts=backup # Rollback

                # Updating Log File
                with open(log_file,mode="w") as T:
                    T.write(f"[ROLLBACK] Batch aborted: Unexpected Error has Occureed")
                print(f"{accounts=}")
                line()
                print("Something Went Wrong")
                return()
            
    line()
    return(accounts)

# MAIN

#  Hardcoded Input
global accounts
accounts={"ACC01": 500.0, "ACC02": 200.0}

# Passing Various Batches of Transactions
Batch_1=[{"acc": "ACC01", "type": "deposit", "amt": 150.0},
            {"acc": "ACC02", "type": "withdraw", "amt": 120.0}
            ]

# Passing Different File names to save Transactions of each Batch
log_file = "transactions1.log"
with open(log_file,mode="w") as T1:
    T1.write(".LOG")

line()
print("BATCH 1")
Try_Except(accounts,Batch_1,log_file)


line()

Batch_2 =[
    {"acc": "ACC01", "type": "deposit", "amt": 50.0},
    {"acc": "ACC02", "type": "withdraw", "amt": 200.0}] # Overdraft!

log_file = "transactions2.log"
with open(log_file,mode="w") as T2:
    T2.write(".LOG")

line()
print("BATCH 2")
Try_Except(accounts,Batch_2,log_file)

Batch_3 =[
    {"acc": "ACC01", "type": "depo", "amt": 50.0},
    {"acc": "ACC02", "type": "withdraw", "amt": 200.0}] # wrong type error expected!


log_file = "transactions3.log"
with open(log_file,mode="w") as T3:
    T3.write(".LOG")

line()
print("BATCH 3")
Try_Except(accounts,Batch_3,log_file)

Batch_4 =[
    {"acc": "ACC01", "type": "DEPOSIT", "amt": 0.0},
    {"acc": "ACC02", "type": " DEPOsit ", "amt": 100.0}]

log_file = "transactions4.log"
with open(log_file,mode="w") as T4:
    T4.write(".LOG")

line()
print("BATCH 4")
Try_Except(accounts,Batch_4,log_file)
line()