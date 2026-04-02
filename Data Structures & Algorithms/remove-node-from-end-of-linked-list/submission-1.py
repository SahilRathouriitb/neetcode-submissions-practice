# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
            temp = head
            k = 0

            while temp != None:
                k = k + 1
                temp = temp.next 

            # removing the first node will be a special case
           
            if k-n == 0:
                return head.next

            temp = head 
            for i in range(1,k-n):
                head = head.next

            head.next = head.next.next

            return temp