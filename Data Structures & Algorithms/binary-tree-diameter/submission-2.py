# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def __init__(self):
        self.m  = 0 

    def max_dia(self, root):
        left_max = 0
        right_max = 0
        if root.left == None and root.right == None:
            return 0

        if root.left != None:
            left_max = 1 + self.max_dia(root.left)
        
        if root.right != None:
            right_max = 1 + self.max_dia(root.right)

        self.m = max(self.m, left_max+right_max)
        return max(left_max, right_max)

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_dia(root)
        return self.m

        