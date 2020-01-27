"""
Created on 27/01/2020
@author: B Akash
"""
"""
Problem statement:
Maintain the List of CompanyShares in a Linked List
 So new CompanyShares can be added or removed easily.
 Do not use any Collection Library to implement Linked List.
"""


class node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, data):
        if self.head == self.tail is None:
            self.head = self.tail = node(data)
        else:
            self.tail.next = node(data)
            self.tail.next.prev = self.tail
            self.tail = self.tail.next

    def delete(self, data):
        if self.head.data == data:
            if self.head == self.tail:
                self.tail = self.head.next
            self.head = self.head.next

        else:
            temp = self.head
            while temp.next is not None and temp.data != data:
                temp = temp.next
            if temp.next is None:
                self.tail = temp.prev
                temp = temp.prev
            else:
                temp.next.prev = temp.prev
                temp.prev.next = temp.next


if __name__ == "__main__":
    print("Company shares")
    llist = LinkedList()

    while True:
        print("Enter\n 1 to add share\n 2 to delete share\n 0 to exit")
        option = int(input())

        if option == 1:
            share = input()
            llist.insert(share)
        elif option == 2:
            share = input()
            llist.delete(share)
        elif option == 0:
            break
        else:
            print("invalid input")
