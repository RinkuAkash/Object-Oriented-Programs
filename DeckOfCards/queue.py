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

    def add_front(self, suit, rank):
        if self.front == self.rear is None:
            self.front = self.rear = node(suit, rank)
        else:
            self.front.prev = node(suit, rank)
            self.front = self.front.prev

    def add_rear(self, suit, rank):
        if self.rear == self.front is None:
            self.rear = self.front = node(suit, rank)
        else:
            self.rear.next = node(suit, rank)
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
        temp = self.front
        while temp is not None:
            print(temp.suit, "of", temp.rank)
            temp = temp.next

    def merge(self, first_node, second_node):
        if first_node is None:
            return second_node

        if second_node is None:
            return first_node

        # checking node ranks and converting to integer
        # to achieve comparision
        first_node_rank = first_node.rank
        second_node_rank = second_node.rank
        checkList = ["2", "3", "4", "5", "6", "7", "8", "9", "10"]

        if first_node_rank in checkList and second_node_rank in checkList:
            first_node_rank = int(first_node_rank)
            second_node_rank = int(second_node_rank)

        if first_node_rank < second_node_rank:
            first_node.next = self.merge(first_node.next, second_node)
            first_node.next.prev = first_node
            first_node.prev = None
            return first_node

        else:
            second_node.next = self.merge(first_node, second_node.next)
            second_node.next.prev = second_node
            second_node.prev = None
            return second_node

    def mergeSort(self, head):
        if head is None:
            return head
        if head.next is None:
            return head

        second_node = self.mid_node(head)
        head = self.mergeSort(head)
        second_node = self.mergeSort(second_node)

        return self.merge(head, second_node)

    # mid method is used to get mid node
    def mid_node(self, head):
        fast = slow = head

        while True:
            if fast.next is None:
                break
            if fast.next.next is None:
                break
            fast = fast.next.next
            slow = slow.next

        mid = slow.next
        slow.next = None
        return mid

    def sort(self):
        self.front = self.mergeSort(self.front)
