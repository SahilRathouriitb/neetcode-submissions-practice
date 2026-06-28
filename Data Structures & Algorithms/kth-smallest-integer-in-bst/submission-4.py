# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.val = None
        self.counter = 0

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # We will again use Depth First Search to solve this question

        if root.left:
            self.kthSmallest(root.left, k)
            if self.counter == k:
                return self.val

        self.counter += 1
        if self.counter == k:
            self.val = root.val
            return self.val
        

        if root.right:
            return self.kthSmallest(root.right, k)
        

        
        