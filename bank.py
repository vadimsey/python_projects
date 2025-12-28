import json

class BankAccount:

    def create_acc(self):
        print('===CREATE ACC===')
        while True:
            name = input('Enter account name(no digit): ').strip()
            if len(name) == 0 or name.isdigit():
                print('=====Enter correct name=====')
            else:
                break

        while True:
            try:
                while True:
                    balance = int(input('Enter account balance: '))
                    if balance < 0:
                        print("=====ENTER CORRECT BALANCE=====")
                    else:
                        break
            except:
                print('=====Enter correct balance=====')
            else:
                break

        accounts = {}
        try:
            with open("accounts.json", "r") as file:
                accounts = json.load(file)
        except:
            accounts = {}

        accounts[name] = balance

        with open("accounts.json", "w") as file:
            json.dump(accounts, file)


    def view_acc(self):
        print('===VIEW ACC===')
        try:
            with open("accounts.json", "r") as file:
                accounts = json.load(file)
        except:
            accounts = {}

        for i, n in enumerate(accounts.items()):
            print(f"{i + 1}. {n[0]} - {n[1]}")

    def withdraw(self):
        print('===WITHDRAW===')
        try:
            with open("accounts.json", "r") as file:
                accounts = json.load(file)
        except:
            accounts = {}

        while True:
            name = input('Enter account name(no digit): ').strip()
            if name not in accounts:
                print("=====THIS ACCOUNT IS NOT VALID=====")
            else:
                break

        balance = accounts[name]

        while True:
            amount = input('Enter amount to withdraw: ')
            if not str(amount).isdigit():
                print('=====Amount cannot be an integer=====')
            elif int(amount) < 0:
                print('=====Amount cannot be negative=====')
            elif int(amount) > balance:
                print('=====Amount cannot be greater than balance=====')
            else:
                break

        accounts[name] = (balance - int(amount))
        with open("accounts.json", "w") as file:
            json.dump(accounts, file)

    def deposit(self):
        print('===DEPOSIT===')
        try:
            with open("accounts.json", "r") as file:
                accounts = json.load(file)
        except:
            accounts = {}

        while True:
            name = input('Enter account name(no digit): ').strip()
            if name not in accounts:
                print("=====THIS ACCOUNT IS NOT VALID=====")
            else:
                break

        while True:
            try:
                amount = int(input('Enter amount to deposit: '))
                if amount < 0:
                    print('=====Amount cannot be negative=====')
            except:
                print("===Invalid amount===")
            else:
                break

        balance = accounts[name]
        accounts[name] = balance + amount
        with open("accounts.json", "w") as file:
            json.dump(accounts, file)


def main():
    bank = BankAccount()


    while True:
        print("\n=====MAIN MENU====")
        print("1. Create new account")
        print("2. View accounts")
        print("3. Deposit")
        print("4. Withdraw")
        print("5. Exit")

        try:
            choice = int(input('Enter choice: '))
        except:
            print("=====Enter correct choice====")

        if choice == 1:
            bank.create_acc()
        elif choice == 2:
            bank.view_acc()
        elif choice == 3:
            bank.deposit()
        elif choice == 4:
            bank.withdraw()
        elif choice == 5:
            exit()
        else:
            print("=====Enter correct choice====")


if __name__ == '__main__':
    main()