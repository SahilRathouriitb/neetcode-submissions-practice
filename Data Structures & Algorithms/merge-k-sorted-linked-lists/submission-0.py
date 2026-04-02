# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        l = []
        for i in lists:
            j = i
            while j!= None:
                l.append(j)
                j = j.next
        # This will give us a list of all the node
        # now we will sort these nodes on the basis of the values they hold

        l.sort(key = lambda i: i.val)

        j = ListNode(None)
        k = j

        for i in l:
            j.next = i
            j = j.next

        return k.next


