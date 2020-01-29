"""
Created on 28/01/2020
@author: B Akash
"""
"""
Problem statement:
Further maintain DateTime of the transaction in a Queue
 implemented using Linked List to indicate when the transactions were done.
"""

from node import node


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def addFront(self, suit, rank):
        if self.front == self.rear is None:
            self.front = self.rear = node(suit, rank)
        else:
            self.front.prev = node(suit, rank)
            self.front = self.front.prev

    def addRear(self, suit, rank):
        if self.rear == self.front is None:
            self.rear = self.front = node(suit, rank)
        else:
            self.rear.next = node(suit, rank)
            self.rear = self.rear.next

    def deleteFront(self):
        if self.front is None:
            return False
        else:
            self.front = self.front.next
            self.front.prev = None
            return True

    def deleteRear(self):
        if self.rear is None:
            return False
        else:
            self.rear = self.rear.prev
            self.rear.next = None
            return True

    def show(self):
        temp=self.front
        while(temp is not None):
            print(temp.suit, "of", temp.rank)
            temp=temp.next
