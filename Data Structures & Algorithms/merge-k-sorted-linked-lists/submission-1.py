# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    

    def sort_sorted_linked_list(self,l1,l2):
    
        if l1 == None:
            return l2
        
        if l2 == None:
            return l1

        a1 = l1
        a2 = l2
        ss = ListNode(None)
        b = ss

        while True:

            if a1 == None:
                ss.next = a2
                break
            
            if a2 == None:
                ss.next = a1
                break

            if a1.val <= a2.val:
                ss.next = a1
                a1 = a1.next
                ss = ss.next 

            else:
                ss.next = a2
                a2 = a2.next
                ss = ss.next

        return b.next
        


    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        if len(lists) == 0:
            return 
        
        if len(lists) == 1:
            return lists[0]

        k = lists[0] 
        for i in range(len(lists)-1):
            k = self.sort_sorted_linked_list(k, lists[i+1] )

        return k          
