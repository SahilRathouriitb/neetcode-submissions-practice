# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.record = dict()

    def build(self, pre_lower, pre_upper,in_lower, in_upper, preorder, inorder):

        if pre_lower == pre_upper:
            return TreeNode(preorder[pre_lower])
        
        
        if pre_lower > pre_upper or in_lower > in_upper:
            return None

        root = TreeNode(preorder[pre_lower])
        
        t = self.record[root.val]

        root.left = self.build(pre_lower + 1, pre_lower + (t-in_lower), in_lower, t-1, preorder, inorder)
        root.right = self.build( pre_lower + (t-in_lower) + 1, pre_upper, t+1, in_upper, preorder, inorder)

        return root

        # Not optimal time, the time taken here is quadratic!

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        for i in range(len(inorder)):
            self.record[inorder[i]] = i

        print(self.record)

        return self.build(0, len(preorder)-1, 0, len(inorder)-1, preorder, inorder)

        



        