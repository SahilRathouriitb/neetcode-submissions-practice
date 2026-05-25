class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class MyCircularQueue:

    def __init__(self, k: int):
        self.start = Node(None)
        a = self.start
        for i in range(k-1):
            a.next = Node(None)
            a = a.next
        
        a.next = self.start

        # Now after this much we have the circular queue

        self.end = self.start
        self.filled = 0 
        self.max_allowed = k
            

    def enQueue(self, value: int) -> bool:
        if self.filled < self.max_allowed:
            if self.end.value != None:
                self.end = self.end.next
            self.end.value = value
            self.filled += 1
            return True

        else:
            return False
        

    def deQueue(self) -> bool:
        if self.filled > 0:
            self.start.value == None
            self.start = self.start.next 
            self.filled -= 1
            return True
        else:
            return False
        

    def Front(self) -> int:
        if self.filled > 0:
            return self.start.value
        else:
            return -1
        

    def Rear(self) -> int:
        if self.filled > 0:
            return self.end.value
        else:
            return -1
        

    def isEmpty(self) -> bool:
        if self.filled == 0:
            return True
        else:
            return False
        

    def isFull(self) -> bool:
        if self.filled == self.max_allowed:
            return True
        else:
            return False