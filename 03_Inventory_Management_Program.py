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

    def add_values(self, item_type, name, weight, price_per_kg):
        self.item[item_type].append(
            {"name": name, "weight": weight, "price_per_kg": price_per_kg}
        )

    def add_total_price(self, item_type, sub_item, total_price):
        self.item[item_type][sub_item]["total_price"] = total_price

    def get_details(self):
        return json.dumps(self.item, indent=4)


class InventoryManager:
    def __init__(self):
        self.inventory_object = InventoryFactory()

    def add_stock(self):
        for _ in range(
            int(input("Enter the number of items you want to add to rice : "))
        ):
            name = input("name : ")
            weight = int(input("weight : "))
            price = int(input("price : "))
            self.inventory_object.add_values("Rice", name, weight, price)

        for _ in range(
            int(input("Enter the number of items you want to add to Pulses : "))
        ):
            name = input("name : ")
            weight = int(input("weight : "))
            price = int(input("price : "))
            self.inventory_object.add_values("Pulses", name, weight, price)

        for _ in range(
            int(input("Enter the number of items you want to add to Wheat : "))
        ):
            name = input("name : ")
            weight = int(input("weight : "))
            price = int(input("price : "))
            self.inventory_object.add_values("Wheat", name, weight, price)

    def calculate_price(self):
        stock = json.loads(self.inventory_object.get_details())

        for item_type in stock:
            for sub_item in range(0, len(stock[item_type])):
                total_price = (
                    stock[item_type][sub_item]["weight"]
                    * stock[item_type][sub_item]["price_per_kg"]
                )
                self.inventory_object.add_total_price(item_type, sub_item, total_price)
        return self.inventory_object.get_details()


if __name__ == "__main__":
    print("Inventory Management Program")
    manager = InventoryManager()
    manager.add_stock()
    print("Final inventory :")
    print(manager.calculate_price())
