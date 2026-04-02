# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        
        temp = head 
        dummy = ListNode(None)
        k = dummy
        j = temp


        while True:

            if j == None:
                break

            if j.val != val:
                k.next = j
                k = k.next 
                j = j.next
                k.next = None

            if j == None:
                break

            if j.val == val:
                j = j.next 

            


        return dummy.next
