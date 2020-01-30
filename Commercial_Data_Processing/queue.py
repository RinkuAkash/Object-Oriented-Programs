from node import node


"""
Created on 28/01/2020
@author: B Akash
"""
"""
Problem statement:
Further maintain DateTime of the transaction in a Queue
 implemented using Linked List to indicate when the transactions were done.
"""


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def add_front(self, dateTime):
        if self.front == self.rear is None:
            self.front = self.rear = node(dateTime)
        else:
            self.front.prev = node(dateTime)
            self.front = self.front.prev

    def add_rear(self, dateTime):
        if self.rear == self.front is None:
            self.rear = self.front = dateTime
        else:
            self.rear.next = node(dateTime)
            self.rear = self.rear.next

    def delete_front(self):
        if self.front is None:
            return False
        else:
            self.front = self.front.next
            self.front.prev = None
            return True

    def delete_rear(self):
        if self.rear is None:
            return False
        else:
            self.rear = self.rear.prev
            self.rear.next = None
            return True

    def show(self):
        print(self.front.data)
        print(self.rear.data)
