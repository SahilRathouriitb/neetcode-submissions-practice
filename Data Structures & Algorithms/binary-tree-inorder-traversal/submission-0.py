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

        if root.left != None:
            self.inorderTraversal(root.left)

        self.store.append(root.val)

        if root.right != None:
            self.inorderTraversal(root.right)
        

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root == None:
            return []
        self.do_it(root)
        return self.store
        
        
