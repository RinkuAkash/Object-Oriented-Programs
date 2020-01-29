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

    def returnBook(self):
        return self.book

    def addEntry(self):
        firstName = input("Enter firstname : ")
        lastName = input("Enter lastname : ")
        if lastName + firstName not in self.book:
            address = input("Enter address : ")
            city = input("Enter city : ")
            state = input("Enter state : ")
            pinCode = int(input("Enter pincode(integers only) : "))
            phoneNumber = int(input("Enter phone number : "))
            self.book[lastName + firstName] = [
                {
                    "address": address,
                    "city": city,
                    "state": state,
                    "pincode": pinCode,
                    "phone-number": phoneNumber,
                }
            ]
            return True
        else:
            return False

    def deleteEntry(self, firstName, lastName):
        del self.book[lastName + firstName]

    def sortBook(self, key):
        if key == "name":
            self.book = {
                key: value
                for key, value in sorted(
                    self.book.items(), key=lambda keyValue: (keyValue[0], keyValue[1])
                )
            }
        else:
            self.book = {
                key: value
                for (key, value) in sorted(
                    self.book.items(),
                    key=lambda keyValue: (keyValue[1][0]["pincode"], keyValue[0]),
                )
            }

    def editEntry(self, firstName, lastName, elementType, element):
        self.book[lastName + firstName][0][elementType] = element

    def view(self, firstName, lastName):
        if lastName + firstName in self.book:
            for key, value in self.book[lastName + firstName][0].items():
                print(key, ":", value)
        else:
            print("User not found")


class AddressBookManager:
    def __init__(self):
        self.books = dict()

    def printBooks(self):
        return self.books

    def addBook(self, name):
        self.books[name] = AddressBook()

    def deleteBook(self, name):
        del self.books[name]


if __name__ == "__main__":
    print("Address Book Management")
    books = AddressBookManager()

    if len(books.printBooks()) == 0:
        print("Your address book is empty create new address book")
        while True:
            name = input("Enter new address book name : ")
            books.addBook(name)
            check = int(input("Enter 0 to add new book\n 1 to select book\n"))
            if check == 1:
                break

    print("Select address book : ")
    listOfBooks = books.printBooks()
    for book in listOfBooks.keys():
        print(book)
    selectedBook = input()+'.json'

    liveBook = listOfBooks[selectedBook]
    flag = True
    while flag:
        print("Your Address Book")
        if len(liveBook.returnBook()) > 0:
            for book in liveBook.returnBook():
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
            lastName, firstName = map(
                str, input("Enter lastname and first name : ").split()
            )
            liveBook.view(firstName, lastName)

        elif option == 1:
            if liveBook.addEntry():
                print("Entry successful")
            else:
                print("Entry failed, User already present")

        elif option == 2:
            lastName, firstName = map(
                str, input("Enter lastname and firstname to delete : ").split()
            )
            liveBook.deleteEntry(firstName, lastName)
            print("Deleted successfully")

        elif option == 3:
            lastName, firstName = map(
                str, input("Enter lastname and firstname :").split()
            )
            elementType = input(
                "Enter type (ex. address,city,state,pincode,phone-number) : "
            )
            element = input("Enter new data : ")
            if elementType == "pincode":
                element = int(element)
            liveBook.editEntry(firstName, lastName, elementType, element)
            print("Edit successful")

        elif option == 4:
            liveBook.sortBook("name")

        elif option == 5:
            liveBook.sortBook("pincode")

        elif option == 6:
            flag = False

        else:
            print("invalid input")
