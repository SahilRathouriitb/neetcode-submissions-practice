# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def check(self, root):

        if root == None:
            return 1

        left_depth = 0
        right_depth = 0
        
        if root.left == None and root.right == None:
            return 0 

        if root.left != None:
            response = self.check(root.left)
            if response == 'f':
                return 'f'
            left_depth = response + 1
        
        if root.right != None:
            response = self.check(root.right)
            if response == 'f':
                return 'f'
            right_depth = response + 1

        if abs(left_depth - right_depth) > 1:
            return 'f'
        else:
            return max(left_depth, right_depth)

        
    def isBalanced(self, root) -> bool:
        response = self.check(root)
        print(response)
        if response == 'f':
            return False
        else: 
            return True
        