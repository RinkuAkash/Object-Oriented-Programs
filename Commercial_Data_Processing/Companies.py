import json


class Companies:
    def __init__(self):
        self.file = open("CompanyShares.json")
        self.List = json.load(self.file)

    def printList(self):
        for info in self.List["StockDetails"]:
            print(info)

    def calculate_price(self, symbol, shares):
        for info in self.List["StockDetails"]:
            if info["StockSymbol"] == symbol and info["NoOfShare"] <= shares:
                return False
            if info["StockSymbol"] == symbol:
                info["NoOfShare"] -= shares
                return info["SharePrice"] * shares
        return False

    def get_price(self, symbol):
        for info in self.List["StockDetails"]:
            if info["StockSymbol"] == symbol:
                return info["SharePrice"]
        return 0

    def add_shares(self, symbol, shares):
        for info in self.List["StockDetails"]:
            if info["StockSymbol"] == symbol:
                info["NoOfShare"] += shares
                break

    def save(self):
        with open("CompanyShares.json", "w") as json_file:
            json.dump(self.List, json_file, indent=4)
