from linked_list import LinkedList
from stack import Stack
from queue import Queue
from stock_account import *
from companies import *
import json

if __name__ == "__main__":
    print("Commercial Data Processing")

    linked_list = LinkedList()
    while True:
        print("Enter 1 to create account\n2 to access account")
        print("3 to add company share\n4 to remove company share")
        print("5 to show companies shares")
        option = int(input())
        if option == 1:
            user_name = input("Enter your name : ")
            account_file = open(user_name + ".json", "w+")
            account = {
                "userDetails": [
                    {
                        "name": user_name,
                        "shares": 0,
                        "total_value": 0,
                        "transactions": [],
                    }
                ],
                "Stocks": [],
            }
            json.dump(account, account_file)
            print("Account created successfully")

        elif option == 2:
            filename = input("Enter filename (with extension) : ")
            try:
                account_file = open(filename)
                break
            except FileNotFoundError:
                print("Account not available")

        elif option == 3:
            share_price = int(input("Enter share price : "))
            stock_name = input("Enter Stock name : ")
            stock_symbol = input("Enter the stock symbol : ")
            number_of_share = int(input("Enter the no. of shares : "))
            data = {
                "SharePrice": share_price,
                "StockName": stock_name,
                "StockSymbol": stock_symbol,
                "NoOfShare": number_of_share,
            }
            linked_list.insert(data)

        elif option == 4:
            stock_symbol = input("Enter Stock symbol : ")
            linked_list.delete(stock_symbol)

        elif option == 5:
            linked_list.show_data()

    account = StockAccount(account_file)
    companies = Companies()
    stack = Stack()
    queue = Queue()
    while True:
        print("Enter")
        print("1 for total value")
        print("2 for buy share")
        print("3 for sell share")
        print("4 save account")
        print("5 print report")
        print("6 print stack")
        print("7 print queue")
        print("0 to exit")

        option = int(input())

        if option == 1:
            print(account.value_of())

        elif option == 2:
            companies.print_stock()
            symbol = input("Enter symbol : ")
            shares = int(input("Enter no of shares : "))
            check = companies.calculate_price(symbol, shares)
            if check is False:
                print("Transaction unsuccessful")
            else:
                amount = check
                account.buy(amount, shares, symbol)
                stack.purchase(symbol)
                queue.add_front(datetime.now().isoformat())
                print("Transaction successfull")

        elif option == 3:
            symbol = input("Enter symbol : ")
            shares = int(input("Enter no. of shares : "))
            share_price = companies.get_price(symbol)
            if share_price > -1 and account.sell(shares, symbol, share_price):
                companies.add_shares(symbol, shares)
                stack.sell()
                queue.delete_rear()
                print("Transaction successful")
            else:
                print("Transaction unsuccessful")

        elif option == 4:
            account.save(filename)
            companies.save()

        elif option == 5:
            account.print_report()

        elif option == 6:
            stack.show()

        elif option == 7:
            queue.show()

        elif option == 0:
            break

        else:
            print("Invalid input")
