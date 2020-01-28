from LinkedList import LinkedList
from StockAccount import *
from Companies import *
import json

if __name__ == "__main__":
    print("Commercial Data Processing")

    llist = LinkedList()
    while True:
        print("Enter 1 to create account\n2 to access account")
        print("3 to add company share\n4 to remove company share")
        print("5 to show companies shares")
        option = int(input())
        if option == 1:
            userName = input("Enter your name : ")
            accountFile = open(userName + ".json", "w+")
            account = {
                "userDetails": [
                    {
                        "name": userName,
                        "shares": 0,
                        "total_value": 0,
                        "transactions": [],
                    }
                ],
                "Stocks": [],
            }
            json.dump(account, accountFile)
            print("Account created successfully")

        elif option == 2:
            filename = input("Enter filename (with extension) : ")
            try:
                accountFile = open(filename)
                break
            except FileNotFoundError:
                print("Account not available")

        elif option == 3:
            SharePrice = int(input("Enter share price : "))
            StockName = input("Enter Stock name : ")
            StockSymbol = input("Enter the stock symbol : ")
            NoOfShare = int(input("Enter the no. of shares : "))
            data = {
                "SharePrice": SharePrice,
                "StockName": StockName,
                "StockSymbol": StockSymbol,
                "NoOfShare": NoOfShare,
            }
            llist.insert(data)

        elif option == 4:
            StockSymbol = input("Enter Stock symbol : ")
            llist.delete(StockSymbol)

        elif option == 5:
            llist.show_Data()

    account = StockAccount(accountFile)
    companies = Companies()
    while True:
        print("Enter")
        print("1 for total value")
        print("2 for buy share")
        print("3 for sell share")
        print("4 save account")
        print("5 print report")
        print("0 to exit")

        option = int(input())

        if option == 1:
            print(account.valueOf())

        elif option == 2:
            companies.printList()
            symbol = input("Enter symbol : ")
            shares = int(input("Enter no of shares : "))
            check = companies.calculate_price(symbol, shares)
            if check is False:
                print("Transaction unsuccessful")
            else:
                amount = check
                account.buy(amount, shares, symbol)
                print("Transaction successfull")

        elif option == 3:
            symbol = input("Enter symbol : ")
            shares = int(input("Enter no. of shares : "))
            share_price = companies.get_price(symbol)
            if share_price > -1 and account.sell(shares, symbol, share_price):
                companies.add_shares(symbol, shares)
                print("Transaction successful")
            else:
                print("Transaction unsuccessful")

        elif option == 4:
            account.save(filename)
            companies.save()

        elif option == 5:
            account.printReport()

        elif option == 0:
            break

        else:
            print("Invalid input")
