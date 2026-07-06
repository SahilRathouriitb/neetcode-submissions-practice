# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        
        temp = root
        if key == temp.val:
            match = temp
            if match.right:
                temp_match = match.right
                k = 0 
                while temp_match.left:
                    k = 1
                    if temp_match.left.left == None:
                        break
                    temp_match = temp_match.left
                
                # temp_match will be the parent 
                # temp_match.left will be the smallest value
                if k == 1:
                    value = temp_match.left.val
                    temp_match.left = temp_match.left.right
                    match.val = value 
                    return root
                else:
                    value = temp_match.val
                    temp_match.left = match.left
                    del match
                    return temp_match
            
            else:
                return temp.left

        else:
            while True:
                if key < temp.val:
                    if temp.left:
                        if key == temp.left.val:
                            break
                        else:
                            temp = temp.left
                    else:
                        return root

                if key > temp.val:
                    if temp.right:
                        if key == temp.right.val:
                            break
                        else: 
                            temp = temp.right
                    else:
                        return root

            # here we have the access to the parent node
            parent = temp
            match = None # kid
            if key > parent.val:
                match = parent.right
            else:
                match = parent.left

            # Case 1: match is a leaf node
            if (not match.left) and (not match.right):
                if match.val > parent.val:
                    parent.right = None
                    return root
                parent.left = None
                return root

            # Case 2: If match has right child or children 
            # In this case we will find the left most child in the right tree
            if match.right:
                temp_match = match.right
                k = 0 
                while temp_match.left:
                    k = 1
                    if temp_match.left.left == None:
                        break
                    temp_match = temp_match.left
                
                # temp_match will be the parent 
                # temp_match.left will be the smallest value
                if k == 1:
                    value = temp_match.left.val
                    temp_match.left = temp_match.left.right
                    match.val = value 
                    return root
                else:
                    value = temp_match.val
                    match.right = temp_match.right
                    match.val = value
                    return root


            # CASE 3: If no right value
            if match.left:
                parent.left = match.left
                return root 

                

                


        
        

        
        

       