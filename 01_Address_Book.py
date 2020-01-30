"""
Created on 25/01/2020
@author: B Akash
"""
"""
Problem statement:
program to maintain address book
"""


class AddressBook:
    def __init__(self):
        self.book = dict()

    def return_book(self):
        return self.book

    def add_entry(self):
        first_name = input("Enter firstname : ")
        last_name = input("Enter lastname : ")
        if last_name + first_name not in self.book:
            address = input("Enter address : ")
            city = input("Enter city : ")
            state = input("Enter state : ")
            pincode = int(input("Enter pincode(integers only) : "))
            phone_number = int(input("Enter phone number : "))
            self.book[last_name + first_name] = [
                {
                    "address": address,
                    "city": city,
                    "state": state,
                    "pincode": pincode,
                    "phone-number": phone_number,
                }
            ]
            return True
        else:
            return False

    def delete_entry(self, first_name, last_name):
        del self.book[last_name + first_name]

    def sort_book(self, key):
        if key == "name":
            self.book = {
                key: value
                for key, value in sorted(
                    self.book.items(),
                    key=lambda key_value: (key_value[0], key_value[1]),
                )
            }
        else:
            self.book = {
                key: value
                for (key, value) in sorted(
                    self.book.items(),
                    key=lambda key_value: (
                        key_value[1][0]["pincode"], key_value[0]
                        ),
                )
            }

    def edit_entry(self, first_name, last_name, element_type, element):
        self.book[last_name + first_name][0][element_type] = element

    def view(self, first_name, last_name):
        if last_name + first_name in self.book:
            for key, value in self.book[last_name + first_name][0].items():
                print(key, ":", value)
        else:
            print("User not found")


class AddressBookManager:
    def __init__(self):
        self.books = dict()

    def print_books(self):
        return self.books

    def add_book(self, name):
        self.books[name] = AddressBook()

    def delete_book(self, name):
        del self.books[name]


if __name__ == "__main__":
    print("Address Book Management")
    books = AddressBookManager()

    if len(books.print_books()) == 0:
        print("Your address book is empty create new address book")
        while True:
            name = input("Enter new address book name : ")
            books.add_book(name)
            check = int(input("Enter 0 to add new book\n 1 to select book\n"))
            if check == 1:
                break

    print("Select address book : ")
    list_of_books = books.print_books()
    for book in list_of_books.keys():
        print(book)
    selected_book = input()

    live_book = list_of_books[selected_book]
    flag = True
    while flag:
        print("Your Address Book")
        if len(live_book.return_book()) > 0:
            for book in live_book.return_book():
                print(book)

        print("select option by entering number")
        options = [
            "View Details",
            "Add Entry",
            "Delete Entry",
            "Edit Entry",
            "Sort by name",
            "Sort by pin code",
            "exit",
        ]
        for index, option in enumerate(options):
            print(index, ":", option)

        option = int(input())

        if option == 0:
            last_name = input("Enter lastname : ")
            first_name = input("Enter firstname : ")
            live_book.view(first_name, last_name)

        elif option == 1:
            if live_book.add_entry():
                print("Entry successful")
            else:
                print("Entry failed, User already present")

        elif option == 2:
            last_name = input("Enter lastname : ")
            first_name = input("Enter firstname : ")
            live_book.delete_entry(first_name, last_name)
            print("Deleted successfully")

        elif option == 3:
            last_name = input("Enter lastname : ")
            first_name = input("Enter firstname : ")
            element_type = input(
                "Enter type (ex. address,city,state,pincode,phone-number) : "
            )
            element = input("Enter new data : ")
            if element_type == "pincode":
                element = int(element)
            live_book.edit_entry(first_name, last_name, element_type, element)
            print("Edit successful")

        elif option == 4:
            live_book.sort_book("name")

        elif option == 5:
            live_book.sort_book("pincode")

        elif option == 6:
            flag = False

        else:
            print("invalid input")
