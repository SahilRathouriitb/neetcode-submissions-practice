# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        right_height = 0 
        left_height = 0
        if root == None:
            return 0

        if root.left == None and root.right == None:
            return 1
        
        if root.left != None:
            left_height = self.maxDepth(root.left)
        if root.right != None:
            right_height = self.maxDepth(root.right)
        
        return 1 + max(left_height, right_height)