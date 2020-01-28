from node import node


class Stack:
    def __init__(self):
        self.head = None
    
    def purchase(self, symbol):
        if self.head is None:
            self.head = node(symbol)
        else:
            self.head.next = node(symbol)
            self.head.next.prev = self.head
            self.head = self.head.next

    def sell(self):
        if self.head is None or self.head.data is None:
            return False
        else:
            self.head = self.head.prev
            return True
    
    def show(self):
        temp=self.head
        while(temp is not None):
            print(temp.data)
            temp=temp.prev