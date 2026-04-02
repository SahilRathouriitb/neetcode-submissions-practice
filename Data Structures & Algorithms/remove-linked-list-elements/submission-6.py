# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        
        dummy = ListNode(None)
        k = dummy
        j = head


        while True:

            if j == None:
                break

            if j.val != val:
                k.next = j
                k = k.next 
                j = j.next
                k.next = None
            
            else:
                j = j.next 


            if j == None:
                break

            
            


        return dummy.next
