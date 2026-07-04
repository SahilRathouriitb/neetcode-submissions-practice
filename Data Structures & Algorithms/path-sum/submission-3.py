# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root == None:
            return False
        
        if targetSum == root.val and root.left == None and root.right == None:
            return True

        if root.left:
           res = self.hasPathSum(root.left, targetSum-root.val)
           if res:
            return True
          
        if root.right:
            res = self.hasPathSum(root.right, targetSum - root.val)
            if res:
                return True

        
        return False


        
        