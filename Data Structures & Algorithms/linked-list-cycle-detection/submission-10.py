# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head == None:
            return False
        
        slow_pointer = head
        fast_pointer = head

        while True:

            # Here we are updating the Fast Pointer
            if fast_pointer.next != None and fast_pointer.next.next != None:
                fast_pointer = fast_pointer.next.next
            else:
                return False
            
            # Now we will perform Comparison
            if slow_pointer == fast_pointer:
                return True
            
            # Now we will update the slow pointer 
            #if slow_pointer.next != None:
            slow_pointer = slow_pointer.next

            #else:
            #    return False