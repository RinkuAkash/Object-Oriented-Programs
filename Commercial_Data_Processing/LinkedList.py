from node import node


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
        if data in self.head.data.values():
            if self.head == self.tail:
                self.tail = self.head.next
            self.head = self.head.next
        else:
            temp = self.head
            while temp.next is not None and data not in temp.data.values():
                temp = temp.next
            if temp.next is None:
                self.tail = temp.prev
                temp = self.tail
                temp.next = None
            else:
                temp.next.prev = temp.prev
                temp.prev.next = temp.next

    def show_Data(self):
        temp = self.head
        while temp is not None:
            print(temp.data)
            temp = temp.next
