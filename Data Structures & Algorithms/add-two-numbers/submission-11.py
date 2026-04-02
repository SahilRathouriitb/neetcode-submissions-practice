# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
       temp1 = l1
       temp2 = l2
       final = ListNode(None)
       head = final
       carry = 0
       while True:
            k = 0

            if temp1 != None:
                k = k + temp1.val 
            
            if temp2 != None:
                k = k + temp2.val

            k = k + carry 

            if k>9:
                carry = 1
                k = k%10
            else:
                carry = 0

            final.next = ListNode(k)
            final = final.next 

            if temp1 != None:
                temp1 = temp1.next 
            if temp2 != None:
                temp2 = temp2.next

            if temp1 == None and temp2 == None and carry == 1:
                final.next = ListNode(carry)
                final = final.next
                break
            if temp1 == None and temp2 == None and carry == 0:
                break

       return head.next

                

        





