# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head != None and head.next != None:
            temp = head
            prev = None

            while temp.next != None:

                current = temp
                next_ele = current.next
                current.next = prev

                prev = current
                temp = next_ele
            
            temp.next = prev
            return temp
        else:
            return head
