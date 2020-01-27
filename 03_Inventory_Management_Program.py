import json


"""
Created on 25/01/2020
@author: B Akash
"""
"""
Problem statement:
Create InventoryManager to manage the Inventory. 
    The Inventory Manager will use InventoryFactory to 
    create Inventory Object from JSON. The InventoryManager 
    will call each Inventory Object in its list to calculate 
    the Inventory Price and then call the Inventory Object to return 
    the JSON String. The main program will be with InventoryManager
"""


class InventoryFactory:
    def __init__(self):
        self.item = dict(Rice=[], Pulses=[], Wheat=[])

    def addValues(self, itemType, name, weight, price_per_kg):
        self.item[itemType].append(
            {"name": name, "weight": weight, "price_per_kg": price_per_kg}
        )

    def addTotalPrice(self, itemType, subItem, totalPrice):
        self.item[itemType][subItem]["total_price"] = totalPrice

    def getDetails(self):
        return json.dumps(self.item, indent=4)


class InventoryManager:
    def __init__(self):
        self.inventoryObject = InventoryFactory()

    def addStock(self):
        for _ in range(
            int(input("Enter the number of items you want to add to rice : "))
        ):
            name = input("name : ")
            weight = int(input("weight : "))
            price = int(input("price : "))
            self.inventoryObject.addValues("Rice", name, weight, price)

        for _ in range(
            int(input("Enter the number of items you want to add to Pulses : "))
        ):
            name = input("name : ")
            weight = int(input("weight : "))
            price = int(input("price : "))
            self.inventoryObject.addValues("Pulses", name, weight, price)

        for _ in range(
            int(input("Enter the number of items you want to add to Wheat : "))
        ):
            name = input("name : ")
            weight = int(input("weight : "))
            price = int(input("price : "))
            self.inventoryObject.addValues("Wheat", name, weight, price)

    def calculatePrice(self):
        stock = json.loads(self.inventoryObject.getDetails())

        for itemType in stock:
            for subItem in range(0, len(stock[itemType])):
                total_price = (
                    stock[itemType][subItem]["weight"]
                    * stock[itemType][subItem]["price_per_kg"]
                )
                self.inventoryObject.addTotalPrice(itemType, subItem, total_price)
        return self.inventoryObject.getDetails()


if __name__ == "__main__":
    print("Inventory Management Program")
    manager = InventoryManager()
    manager.addStock()
    print("Final inventory :")
    print(manager.calculatePrice())
