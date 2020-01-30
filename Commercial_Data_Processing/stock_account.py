import json
from datetime import datetime


"""
Created on 28/01/2020
@author: B Akash
"""
"""
Problem statement:
StockAccount.java implements a data type that might be used by a financial
 institution to keep track of customer information.
 The StockAccount class implements following methods

The StockAccount class also maintains a list of CompanyShares object
 which has Stock Symbol and Number of Shares as well as DateTime of
 the transaction. When buy or sell is initiated StockAccount checks
  if CompanyShares are available and accordingly update or create an Object.
"""


class StockAccount:
    def __init__(self, filename):
        self.account = json.load(filename)

    def value_of(self):
        return self.account["userDetails"][0]["total_value"]

    def buy(self, amount, shares, symbol):
        self.account["userDetails"][0]["total_value"] += amount
        self.account["userDetails"][0]["shares"] += shares
        if symbol in self.account["stocks"]:
            self.account["stocks"][symbol] += shares
        else:
            self.account["stocks"][symbol] = shares
        time = datetime.now().isoformat()
        self.account["userDetails"][0]["transactions"].append(
            {
                "Type": "BOUGHT",
                "symbol": symbol,
                "shares": shares,
                "value": amount,
                "time": time,
            }
        )

    def sell(self, shares, symbol, share_price):
        if symbol not in self.account["stocks"]:
            return False
        if self.account["stocks"][symbol] >= shares:
            self.account["stocks"][symbol] -= shares
            self.account["userDetails"][0]["shares"] -= shares
            self.account["userDetails"][0]["total_value"] -= shares * share_price
            time = datetime.now().isoformat()
            self.account["userDetails"][0]["transactions"].append(
                {
                    "Type": "SOLD",
                    "symbol": symbol,
                    "shares": shares,
                    "value": shares * share_price,
                    "time": time,
                }
            )
            return True
        else:
            return False

    def save(self, filename):
        with open(filename, "w") as json_file:
            json.dump(self.account, json_file, indent=4)

    def print_report(self):
        user_details = self.account["userDetails"][0]
        print("--------------------------------------------")
        print("Name :", user_details["name"])
        print("Shares :", user_details["shares"])
        print("Total value :", user_details["total_value"])
        print("Transaction")
        for info in user_details["transactions"]:
            print(info)
        print("Stocks")
        for symbol in self.account["stocks"]:
            print(symbol, ":", self.account["stocks"][symbol])
        print("--------------------------------------------")
