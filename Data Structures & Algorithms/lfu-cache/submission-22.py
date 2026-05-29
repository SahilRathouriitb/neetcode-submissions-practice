class Node:
    def __init__(self, key = None, value = None):
        self.value = value
        self.key = key
        self.next = None
        self.prev = None

class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.frequency = {}
        self.cache = {}
        self.order = {}
        self.filled = 0 


    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        else:
            # We need to uplift it though in the order 
            node = self.cache[key]

            previous_node = node.prev
            next_node = node.next

            previous_node.next = next_node
            next_node.prev = previous_node

            if (next_node.key == None) and (previous_node.key == None):
                self.order.pop(self.frequency[key])
            
            
            self.frequency[key] += 1
            new_order = self.frequency[key]

            # now we will uplift this order
            if  new_order not in self.order:
                self.order[self.frequency[key]] = self.create_structure(node)
            else:
                self.insert_into_existing_structure(node, key)
            
            return self.cache[key].value 


    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # if key is aready there, we shall firstly update its value

            node = self.cache[key]
            node.value = value
            # now we should shoudl update this in oder
            previous_node = node.prev
            next_node = node.next

            previous_node.next = next_node
            next_node.prev = previous_node

            self.frequency[key] += 1
            
            if self.frequency[key] in self.order:
                dummy_left = self.order[self.frequency[key]][0]
                node.prev = dummy_left
                node.next = dummy_left.next
                dummy_left.next.prev = node
                dummy_left.next = node
            else:
                structure = self.create_structure(node)
                self.order[self.frequency[key]] = structure


        elif key not in self.cache and (self.filled < self.capacity):
            # This is a new element
            new_node = Node(key,value) 
            self.cache[key] = new_node
            self.frequency[key] = 1
            if self.frequency[key] not in self.order:
                self.order[self.frequency[key]] = self.create_structure(new_node)
            else:
                self.insert_into_existing_structure(new_node, key)
            self.filled += 1


        elif (key not in self.cache) and (self.filled == self.capacity):
            # Firstly we will have to remove an entry and then we will have to add an entry
            # for this we will refer self.order # i will have to find 
            min_frequency = min(list(self.order.keys()))
            left_dummy = self.order[min_frequency][0]
            target = left_dummy.next 
            right_node = target.next

            left_dummy.next = right_node
            right_node.prev = left_dummy

            if right_node.key == None:
                # We need to remove this frequency from oder 
                self.order.pop(min_frequency)
                
                
            target_key = target.key 
            self.frequency.pop(target_key)
            self.cache.pop(target_key)
            self.filled -= 1

            # Now adding the new element 
            new_node = Node(key,value) 
            self.cache[key] = new_node
            self.frequency[key] = 1
            if self.frequency[key] not in self.order:
                self.order[self.frequency[key]] = self.create_structure(new_node)
            else:
                self.insert_into_existing_structure(new_node, key)
            self.filled += 1

    
    def insert_into_existing_structure(self, node, key):

        dummy_right = self.order[self.frequency[key]][1]
        last_second = dummy_right.prev
        
        node.next = dummy_right
        node.prev = last_second

        last_second.next = node
        dummy_right.prev = node

        

    def create_structure(self, node):
        dummy_left = Node()
        dummy_right = Node()
        
        node.prev = dummy_left
        dummy_left.next = node

        node.next = dummy_right
        dummy_right.prev = node
        return (dummy_left, dummy_right)
    
    