"""
Created on 27/01/2020
@author: B Akash
"""
"""
Problem statement:
Further maintain the Stock Symbol Purchased or Sold in
 a Stack implemented using Linked List to indicate transactions done.
 """


class node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.count = 0

    def purchase(self, share):
        if self.head is None:
            self.head = node(share)
        else:
            self.head.next = node(share)
            self.head.next.prev = self.head
            self.head = self.head.next
        self.count += 1

    def sell(self):
        if self.head is None or self.head.data is None:
            return False
        else:
            self.head = self.head.prev
            self.count -= 1
            return True


if __name__ == "__main__":
    print("Stock transactions")
    stack = LinkedList()

    while True:
        print("Enter")
        print("1 to purchase")
        print("2 to sell")
        print("3 to count stocks")
        print("0 to exit")

        option = int(input())

        if option == 1:
            share = input("Enter stock symbol : ")
            stack.purchase(share)
        elif option == 2:
            if stack.sell():
                print("Stock sold successfully")
            else:
                print("Insufficient stocks to sell")
        elif option == 3:
            print("You have %d number of stocks" % stack.count)
        elif option == 0:
            break
        else:
            print("Invalid input")
