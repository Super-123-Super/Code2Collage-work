import mysql.connector

connection = mysql.connector.connect(user = 'root', database = 'example', password = 'SwimDolphin45')


class Account:
    def __init__(self, account_id, password, username, full_name, balance):
        self.account_id = account_id
        self.username = username
        self.password = password
        self.balance = balance
        self.full_name = full_name

    def __str__(self):
        return f"Account({self.account_id}, Full Name: {self.full_name}, Username: {self.username},Balance: {self.balance})"

def create_account(username, password, balance, full_name):
    cursor = connection.cursor()
    addData = (f"INSERT INTO account (username, password, balance, full_name) VALUES ('{username}', '{password}', {balance}, '{full_name}')")
    cursor.execute(addData)
    row_id = cursor.lastrowid
    connection.commit()
    cursor.close()
    return row_id

def delete_account(id):
    cursor = connection.cursor()
    addData = (f"DELETE FROM account where account_id = {id}")
    cursor.execute(addData)
    connection.commit()
    cursor.close()


def get_account(username, password):
    cursor = connection.cursor()
    testQuery = (f"select * from account where username = '{username}' and password = '{password}'")
    cursor.execute(testQuery)
    account_data = cursor.fetchone()
    if account_data:
        account = Account(account_data[0], account_data[1], account_data[2], account_data[3], account_data[4])
        return account
    

def check_account_balance(account):
    print(f"balance: {account.balance}")
    return account

def deposit(money):
    account.balance = float(account.balance) + money
    return account.balance

def withdraw(money):
    account.balance = float(account.balance) - money
    return account.balance
# deposit(num)

# withdraw(num)

def menu():
    print("Menu")
    print("1. Login")
    print("2. Sign Up")
    option = int(input("-> "))
    if option == 1:
        login()
    elif option == 2:
        sign_up()
    else:
        print("unavaible")
        menu()

#   to options login or crate account
#   if i login then get 3 options check balance, withdraw or deposit otherwise create account

#create a sign up methed so the user can make an account

def sign_up():
    usernamei = str(input("Whats your username -> "))
    passwordi = str(input("Whats your password -> "))
    account.username = usernamei
    account.password = passwordi
    print("successfuly signed up")






def login():
    print(" ")
    print("Login Options")
    print("1. Check Balance")
    print("2. Withdraw")
    print("3. Deposit")
    option = int(input("-> "))
    if option == 1:
        check_account_balance(account)
    elif option == 2:
        money = float(input("Withdraw -> $"))
        balance = withdraw(money)
        print(f"New Balance = {balance}")
    elif option == 3:
        money = float(input("Deposit -> $"))
        balance = deposit(money)
        print(f"New Balance = {balance}")
    else:
        print("unavaible")
        login()

    


#check_account_balance(account1)
#add_account_money(account1, 100)
if __name__ == '__main__':
    create_account("CO","4631",40.76 ,"Chidera Okoye")
    account = get_account("CO","4631")
    if account:
        print(account)
    connection.close()
    menu()

