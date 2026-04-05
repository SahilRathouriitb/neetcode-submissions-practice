# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

            if left == right:
                  return head

            temp = head 
            a1st_half = None
            lft = None
            rgt = None

            for i in range(1,right+1):

                if (left != 1) and i == (left-1):
                      a1st_half = temp
                      
                if i == left:
                    lft = temp
                
                if i == right:
                    rgt = temp

                temp = temp.next


            a2nd_half = rgt.next
            rgt.next = None
            head_reversed, tail_reversed = self.reverse(lft)



            if left != 1:
                #a1st_half.next = None 
                a1st_half.next = head_reversed
                tail_reversed.next = a2nd_half
                return head
            
                  
            else:
                  tail_reversed.next = a2nd_half
                  return head_reversed

    def reverse(self, head):
            
        temp = head
        k = None
        while True:

            if temp == None:
                break
            
            a = temp.next 
            temp.next = k
            k = temp
            temp = a
        return k, head




        