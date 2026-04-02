# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 1:
             return head
            

        dic = {}

        i = 1
        j = 1
        temp = head
        top = temp

        while True:

            if j == k:
                dic[i] = top
                ice_cream = temp.next 
                temp.next = None
                top = ice_cream
                i = i + 1
                j = 1
                temp = top

            if temp == None:
                break

            temp = temp.next 
            if temp == None:
                dic[i] = top
                break
            j = j + 1
    
        for i in dic:
            dic[i] = self.reverse_linked_list(dic[i],k)

        


        top = dic[1]
        for i in range(1, len(dic)):
             
            while top.next != None:
                 
                 top = top.next
            
            top.next = dic[i+1]
            top = top.next

        return dic[1]

    def reverse_linked_list(self,list,k):
        
        # Let's count the number of nodes in the Linked List
        count = 0 
        temp = list
        while temp != None:
             count = count + 1
             temp = temp.next 
             
        
        if count < k:
             return list 
        

        temp = list
        a = None
        prev = None

        while True:
            a = temp.next 
            temp.next = prev

            prev = temp
            temp = a 

            if temp == None:
                break
        
        return prev
        
        
                 
             

        


