# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution: 

    def match(self, root1, subroot) -> bool:
        if (root1.left == None and subroot.left != None) or (root1.right == None and subroot.right != None):
            return False

        if (root1.left != None and subroot.left == None) or (root1.right != None and subroot.right == None):
            return False
        
        if root1.left != None:
            if root1.left.val == subroot.left.val:
                response = self.match(root1.left, subroot.left)
                if response == False:
                    return False
            else:
                return False

        if root1.right != None:
            if root1.right.val == subroot.right.val:
                response = self.match(root1.right, subroot.right)
                if response == False:
                    return False
            else:
                return False

        return True        
        
            


    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        if root.val == subRoot.val:
            response = self.match(root, subRoot)
            if response == True:
                return True
            

        if root.left != None:
            response = self.isSubtree(root.left,subRoot)
            if response == True:
                    return True
        
        if root.right != None:
            response = self.isSubtree(root.right,subRoot)
            if response == True:
                    return True

        return False


        