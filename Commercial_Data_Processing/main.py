from StockAccount import *
from Companies import *
import json

if __name__=='__main__':
    print("Commercial Data Processing")
    while True:
        print("Enter 1 to create account\n 2 to access account")
        option = int(input())
        if option == 1:
            userName= input("Enter your name : ")
            accountFile=open(userName+".json","w+")
            account={'userDetails':[{
                'name':userName,
                'shares':0,
                'total_value':0,
                'transactions':[]
                }],
                'Stocks':[]
                }
            json.dump(account,accountFile)
            print("Account created successfully")
        
        elif option == 2:
            filename=input("Enter filename (with extension) : ")
            try:
                accountFile=open(filename)
                break
            except FileNotFoundError:
                print("Account not available")
    
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

        option =int(input())

        if option == 1:
            print(account.valueOf())
        
        elif option == 2:
            companies.printList()
            symbol=input("Enter symbol : ")
            shares=int(input("Enter no of shares : "))
            check=companies.calculate_price(symbol,shares)
            if check is False:
                print("Transaction unsuccessful")
            else:
                amount=check
                account.buy(amount, shares, symbol)
                print("Transaction successfull")
        
        elif option == 3:
            symbol=input("Enter symbol : ")
            shares=int(input("Enter no. of shares : "))
            share_price = companies.get_price(symbol)
            if share_price>-1 and account.sell(shares, symbol, share_price):
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