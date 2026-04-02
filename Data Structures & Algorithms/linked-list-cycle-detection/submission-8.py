# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        top = head

        if head == None or head.next == None:
            return False
            
        
        while head.next.next != None and top.next.next != None:
            
            a = head
            b = top.next.next 
            

            if a == b:
                return True

            head = head.next
            top = b

        return False