# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.store = []
    
    def do_it(self, root):
        if root.left == None and root.right == None:
            self.store.append(root.val)
            return 
        
        self.store.append(root.val)

        if root.left != None:
            self.preorderTraversal(root.left)

        if root.right != None:
            self.preorderTraversal(root.right)

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root == None:
            return []
        self.do_it(root)
        return self.store
        
        

        
        
     