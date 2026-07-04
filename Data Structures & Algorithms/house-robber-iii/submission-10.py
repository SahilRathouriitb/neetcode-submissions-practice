# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def __init__(self):
        self.record = {}

    def money(self,root, flag):

        if (root, flag) in self.record:
            return self.record[(root,flag)]
        
        sum = 0
        flag = flag
        v1 = 0
        v2 = 0
        

        if flag == 1:
            sum = sum + root.val
            if root.left:
                v1 = self.money(root.left, 0)
            if root.right:
                v2 = self.money(root.right,0)
            
            self.record[(root,flag)] = sum + v1 + v2   
            return sum + v1 + v2
        
        if flag == 0:
            if root.left:
                v1_1 = self.money(root.left, 0)
                v1_2 = self.money(root.left,1)
                v1 = max(v1_1, v1_2)
            if root.right:
                v2_1 = self.money(root.right, 0)
                v2_2 = self.money(root.right, 1)
                v2 = max(v2_1, v2_2)
            self.record[(root,flag)] = sum + v1 + v2
            return sum + v1 + v2

        
            


    def rob(self, root: Optional[TreeNode]) -> int:

        val1 = self.money(root, 1)
        val2 = self.money(root, 0)

        return max(val1, val2)

        