# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        l1 = list1
        l2 = list2
        sorted = ListNode("Start")
        a = sorted


        while True:

            if l1 == None:
                sorted.next = l2
                break
            elif l2 == None:
                sorted.next = l1
                break

            if l1.val<=l2.val:
                sorted.next = l1
                sorted = sorted.next
                l1 = l1.next 

            else:
                sorted.next = l2
                sorted = sorted.next
                l2 = l2.next

        return a.next

            