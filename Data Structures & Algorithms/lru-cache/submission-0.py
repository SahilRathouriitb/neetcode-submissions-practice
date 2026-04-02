class Node:

    def __init__(self, key, value):

        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.counter = 0 
        self.dic = {}
        self.least = None
        self.most = None
        self.dummy_most = Node(None, None)
        self.dummy_least = Node(None, None)
        

    def get(self, key: int) -> int:
        if key in self.dic:
            
            if self.dic[key] != self.most:
                # It has been updated, now we need to push it in front of the list
                self.dic[key].prev.next = self.dic[key].next
                self.dic[key].next.prev = self.dic[key].prev
                self.dic[key].next = self.dummy_most
                self.dic[key].prev = self.most
                self.most.next = self.dic[key]
                self.most = self.dic[key]
                self.least = self.dummy_least.next

            return self.most.value

        
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:


        if key in self.dic:

            self.dic[key].value = value

            if self.dic[key] != self.most:
                # It has been updated, now we need to push it in front of the list
                self.dic[key].prev.next = self.dic[key].next
                self.dic[key].next.prev = self.dic[key].prev
                self.dic[key].next = self.dummy_most
                self.dic[key].prev = self.most
                self.most.next = self.dic[key]
                self.most = self.dic[key]
                self.least = self.dummy_least.next

        elif key not in self.dic and (self.counter < self.capacity) and (self.counter == 0):
            # If this is the condition it means it is the first element in the cache 
            new_node = Node(key,value)

            self.dic[key] = new_node
            self.least = new_node
            self.most = new_node

            self.most.next = self.dummy_most
            self.dummy_most.prev = self.most

            self.least.prev = self.dummy_least
            self.dummy_least.next = self.least

            self.counter = self.counter + 1


        elif key not in self.dic and (self.counter < self.capacity) and (self.counter != 0):
            # So here we will add a new node, this will move to the front
            
            new_node = Node(key, value)
            self.dic[key] = new_node
            
            # Let's add this new node to the doubly LL
            new_node.prev = self.most
            self.most.next = new_node
            self.most = new_node

            self.most.next = self.dummy_most
            self.dummy_most.prev = self.most

            self.counter = self.counter + 1


        elif key not in self.dic and (self.counter == self.capacity):

            if self.capacity == 1:

                self.most.key = key
                self.most.value = value
                self.dic = {}
                self.dic[key] = self.most
            
            else:

                # Step 1 - Elimination
                k = self.least
                j = self.least.next
                j.prev = self.dummy_least
                self.least = j
                self.dummy_least.next = self.least

                key2 = k.key
                self.dic.pop(key2)
                self.counter = self.counter -1

                # Step 2 - Addition
                new_node = Node(key, value)
                self.dic[key] = new_node

                new_node.prev = self.most
                self.most.next = new_node
                self.most = new_node

                self.most.next = self.dummy_most
                self.dummy_most.prev = self.most
                self.counter = self.counter +1

        
