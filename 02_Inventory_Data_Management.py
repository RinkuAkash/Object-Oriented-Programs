import json

"""
Created on 25/01/2020
@auther: B Akash
"""
"""
Problem Statement:
    Create a JSON file having Inventory Details for Rice, Pulses and Wheats
        with properties name, weight, price per kg.
"""

json_data = {
    "Rice": [
        {"name": "Basmati", "weight": 1000, "price": 95},
        {"name": "Kurnool", "weight": 840, "price": 44},
    ],
    "Pulses": [
        {"name": "channa", "weight": 900, "price": 112},
        {"name": "moong", "weight": 850, "price": 129},
    ],
    "Wheat": [
        {"name": "indian", "weight": 830, "price": 55},
        {"name": "golden", "weight": 790, "price": 40},
    ],
}


class Inventory:
    def __init__(self, key):
        if key == 1:
            self.item = "Rice"
        elif key == 2:
            self.item = "Pulses"
        elif key == 3:
            self.item = "Wheat"
        self.inventory = json.dumps(json_data, indent=4)

    def get_list(self):
        item_type = self.item
        unload = json.loads(self.inventory)
        return unload[item_type]


print("Inventory Data Management")
print("Enter\n1 for Rice\n2 for Pulses\n3 for Wheats")

key = int(input())

if key in [1, 2, 3]:
    obj = Inventory(key)
    items = obj.get_list()

    for item_index in range(0, len(items)):
        print(
            "ID :",
            item_index,
            ", Type :",
            items[item_index]["name"],
            ", Stock :",
            items[item_index]["weight"],
            ", Price :",
            items[item_index]["price"],
        )

    ID = int(input("Enter item ID: "))
    quantity = int(input("Enter quantity(in kgs) : "))

    try:
        if quantity <= items[ID]["weight"]:
            bill = json.dumps(
                {
                    "item_name": items[ID]["name"],
                    "Quantity": quantity,
                    "Cost": quantity * items[ID]["price"],
                },
                indent=4,
            )
            print("your bill :", bill)
        else:
            print("sorry! stock is less than required")

    except IndexError:
        print("Invalid Id")

else:
    print("Invalid input")
