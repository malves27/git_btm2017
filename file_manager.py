import os

client_filename = "clients.txt"
transaction_filename = "transactions.txt"

def add_client(client_name):
    F = open(client_filename,"w")
    F.write(client_name)
    F.close()
      
def add_transaction(debtor, creditor, amount):
    F = open(transaction_filename, "w")
    F.write('\t'.join([debtor, creditor, amount]))
    F.close()
        
def get_clients():
    pass

def get_transactions():
    pass
    



