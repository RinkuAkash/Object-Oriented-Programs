"""
Created on 25/01/2020
@author: B Akash
"""
"""
Problem statement:
Write a program to read in Stock Names, Number of Share, Share Price. 
Print a Stock Report with total value of each Stock and the total value of Stock.
"""


class Stock:
    def __init__(self):
        self.stocks = []

    def addValues(self, name_of_share, no_of_shares, price_of_share):
        self.stocks.append([name_of_share, no_of_shares, price_of_share])


class Stock_portfolio(Stock):
    def __init__(self):
        super().__init__()

    def printPortfolio(self):
        for stock in self.stocks:
            print(stock[0], "|", stock[1], "|", stock[2], "|", stock[2] * stock[1])


if __name__ == "__main__":

    print("Enter the number of stocks")
    stock = Stock_portfolio()

    for _ in range(int(input())):
        name_of_share = input("Enter share name: ")
        no_of_shares = int(input("Enter no. of shares: "))
        price_of_share = int(input("Enter price of each share: "))
        stock.addValues(name_of_share, no_of_shares, price_of_share)

    print(
        "Name of the share",
        "|",
        "No. of shares",
        "|",
        "Price of the share",
        "|",
        "Total Value",
    )
    stock.printPortfolio()
