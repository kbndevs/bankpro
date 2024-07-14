class Account:
    def __init__(self, account_number, balance=0.0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return True
        return False

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return True
        return False

    def __str__(self):
        return f"Account Number: {self.account_number}, Balance: {self.balance:.2f}"


class Customer:
    def __init__(self, customer_id, name):
        self.customer_id = customer_id
        self.name = name
        self.accounts = []

    def add_account(self, account):
        self.accounts.append(account)

    def __str__(self):
        account_list = "\n".join([str(account) for account in self.accounts])
        return f"Customer ID: {self.customer_id}, Name: {self.name}\nAccounts:\n{account_list}"


class Bank:
    def __init__(self):
        self.customers = {}
        self.accounts = {}

    def add_customer(self, customer_id, name):
        if customer_id not in self.customers:
            customer = Customer(customer_id, name)
            self.customers[customer_id] = customer
            return customer
        return None

    def add_account(self, customer_id, account_number):
        if customer_id in self.customers and account_number not in self.accounts:
            account = Account(account_number)
            self.accounts[account_number] = account
            self.customers[customer_id].add_account(account)
            return account
        return None

    def deposit_money(self, account_number, amount):
        if account_number in self.accounts:
            return self.accounts[account_number].deposit(amount)
        return False

    def withdraw_money(self, account_number, amount):
        if account_number in self.accounts:
            return self.accounts[account_number].withdraw(amount)
        return False

    def transfer_money(self, from_account_number, to_account_number, amount):
        if (from_account_number in self.accounts and
                to_account_number in self.accounts and
                self.accounts[from_account_number].withdraw(amount)):
            return self.accounts[to_account_number].deposit(amount)
        return False

    def list_customers(self):
        return [str(customer) for customer in self.customers.values()]


bank = Bank()

while True:
    print("Welcome to eShikhon Bank PLC")
    print("Please choose an option:")
    print("1. Add Customer")
    print("2. Add Account")
    print("3. Deposit Money")
    print("4. Withdraw Money")
    print("5. Transfer Money")
    print("6. List Customers ")
    print("7. Exit")

    option = input("Enter your choice: ")

    if option == "1":
        customer_id = input("Enter Customer ID: ")
        name = input("Enter Customer Name: ")
        if bank.add_customer(customer_id, name):
            print(f"Customer {name} added successfully.")
        else:
            print("Add Customer Failed")

    elif option == "2":
        customer_id = input("Enter Customer ID: ")
        account_number = input("Enter Account Number: ")
        if bank.add_account(customer_id, account_number):
            print(f"Account {account_number} added successfully.")
        else:
            print("Account Not added.")

    elif option == "3":
        account_number = input("Enter Account Number: ")
        amount = float(input("Enter Amount to Deposit: "))
        if bank.deposit_money(account_number, amount):
            print("Deposit successful.")
        else:
            print("Deposit Not Successful.")

    elif option == "4":
        account_number = input("Enter Account Number: ")
        amount = float(input("Enter Amount to Withdraw: "))
        if bank.withdraw_money(account_number, amount):
            print("Withdrawal successful.")
        else:
            print("Withdrawal Not Successful.")

    elif option == "5":
        from_account_number = input("Enter From Account Number: ")
        to_account_number = input("Enter To Account Number: ")
        amount = float(input("Enter Amount to Transfer: "))
        if bank.transfer_money(from_account_number, to_account_number, amount):
            print("Transfer successful.")
        else:
            print("Transfer Money Not Successful.")

    elif option == "6":
        customers = bank.list_customers()
        if customers:
            for customer in customers:
                print(customer)
        else:
            print("List Customers Not Found.")

    elif option == "7":
        print("Thank You! Exiting eShikhon Bank PLC. Goodbye!")
        break
