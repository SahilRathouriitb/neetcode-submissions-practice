"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head == None:
            return None

        # This pointer will be there at the head and this pointer will traverse the LL and we will make a new copy
        top = head 
        a = Node(top.val)
        b = a # This is a pointer at the head of the new Linked List this will be the head
        map = {top:a, None: None}

        while top.next != None:
            
            top = top.next 
            a.next = Node(top.val)
            a = a.next
            map[top] = a
        

        # So b is the new copied Linked List and the new created dict basically has the original node vs copied node

        top = head # Pointer for the original 
        k = b # Pointer for the created copy 
        k.random = map[top.random]
        while top.next != None:
            top = top.next 
            k = k.next 
            k.random = map[top.random]

        return b 