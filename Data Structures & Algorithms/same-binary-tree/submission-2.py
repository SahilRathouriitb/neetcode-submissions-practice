# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        if p == None and q == None:
            return True

        if (p == None and q != None) or (p != None and q == None):
            return False

        if p.val == q.val:
            if (p.left and (not q.left)) or (q.left and (not p.left)) or (p.right and (not q.right)) or (q.right and (not p.right)):
                return False
            if p.left and q.left:
                result1 = self.isSameTree(p.left, q.left)
                if (not result1):
                    return False 
            if p.right and q.right:
                result2 = self.isSameTree(p.right, q.right)
                if (not result2):
                    return False
            return True
        else:
            return False