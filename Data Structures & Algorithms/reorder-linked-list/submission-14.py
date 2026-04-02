# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
      

        # firstly i will have to count the number of elements in the LL
        a = head

        k = 0
        while a!= None:
            k = k+1
            a = a.next

        if k == 1 or k ==2:
            head = head
        
        else:
            # This k has the number of nodes in the linked list, we need the middle
            mid = k//2

            # Now i need to break this linked list into two and i need both the head pointers

            temp  = head
            A = temp
            B_ = None

            for i in range(mid):

                if i == (mid)-1:
                    B_ = temp.next 
                    temp.next = None
                    break
                
                temp = temp.next
            
            

            # Now we have the two parts and we need to reverse part B
            previous = None
            current = B_
            if B_.next != None:

                while True:
                    if current.next == None:
                        break

                    next = current.next
                    current.next = previous 
                    previous = current
                    current = next

                current.next = previous
            rev_B = current
            

            # Now we have our A ready and reverse B ready

            final = A
            s = final


            while True:
                
                if A.next != None: 
                    A = A.next
                else:
                    final.next = rev_B
                    break 
                
                
                final.next = rev_B
                final = final.next
                rev_B = rev_B.next
               
                
                final.next = A
                final = final.next

            