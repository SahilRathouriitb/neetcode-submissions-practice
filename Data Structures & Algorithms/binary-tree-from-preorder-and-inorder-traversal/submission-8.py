# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        if not preorder:
            return None

        root = TreeNode(preorder[0])
        
        val = None
        for i in range(len(inorder)):
            if inorder[i] == root.val:
                val = i
                break


        root.left = self.buildTree(preorder[1:val+1], inorder[0:val])
        root.right = self.buildTree(preorder[val+1:], inorder[val+1:])

        return root

        

        



        