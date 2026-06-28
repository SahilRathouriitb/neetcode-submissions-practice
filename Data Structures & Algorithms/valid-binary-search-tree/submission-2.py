# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def __init__(self):
        self.upper = [1001]
        self.lower = [-1001]

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
    
        res1 = True
        res2 = True


        if root.left:
            self.upper.append(root.val)
            if (root.left.val >= self.upper[-1]) or (root.left.val <= self.lower[-1]):
                return False
            res1 = self.isValidBST(root.left)
            self.upper.pop()


        if root.right:
            self.lower.append(root.val)
            if (root.right.val <= self.lower[-1]) or (root.right.val >= self.upper[-1]):
                return False
            res2 = self.isValidBST(root.right)
            self.lower.pop()

        if res1 and res2:
            return True
        else:
            return False       
        
        