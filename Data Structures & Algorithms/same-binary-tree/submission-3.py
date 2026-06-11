# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        # Handles the edge case
        if p == None and q == None:
            return True
        # Handling the edge case, where input is None
        if (p == None and q != None) or (p != None and q == None):
            return False

        ## Proper code

        if p.val == q.val:
            if (p.left and (not q.left)) or (q.left and (not p.left)) or (p.right and (not q.right)) or (q.right and (not p.right)):
                return False

            
            result1 = self.isSameTree(p.left, q.left)
            if (not result1):
                    return False 

            
            result2 = self.isSameTree(p.right, q.right)
            if (not result2):
                    return False
            return True

        else:
            return False