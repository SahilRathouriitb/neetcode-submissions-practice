# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        temp1 = l1
        temp2 = l2
        num1 = 0
        num2 = 0
        digit = 1
        while True:

            if temp1 != None:
                num1 = num1 + digit*(temp1.val)
                temp1 = temp1.next

            if temp2 != None:
                num2 = num2 + digit*(temp2.val)
                temp2 = temp2.next

            if (temp1 == None) and (temp2 == None):
                break

            digit = digit*10

        sum = num1+num2
        k = sum%10
        sum = sum//10
        a = ListNode(k)
        head = a
        while sum != 0:
             a.next = ListNode(sum%10)
             a = a.next 
             sum = sum//10

             

        return head



