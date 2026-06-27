# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.stack = []
        self.counter = 1 # 1 for root

    def good(self, root: TreeNode):
        check = 0 
        if len(self.stack) == 0:
            self.stack.append(root.val)
        else:
            if self.stack[-1] < root.val:
                if root.left or root.right:
                    self.stack.append(root.val)
                    check = 1
        
        if root.left != None:
            if root.left.val >= self.stack[-1]:
                self.counter += 1
            self.good(root.left)
        
        if root.right != None:
            if root.right.val >= self.stack[-1]:
                self.counter += 1
            self.good(root.right)
        if check == 1:
            self.stack.pop()
    
    def goodNodes(self, root: TreeNode) -> int:
        self.good(root)
        return self.counter




        
        


        