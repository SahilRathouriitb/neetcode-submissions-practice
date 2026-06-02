# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.output = []

    def max_depth(self,root):
        queue = deque([root])

        while len(queue) > 0:
            level_size = len(queue)
            temp_list = []
            for i in queue:
                temp_list.append(i.val)
            self.output.append(temp_list)
            
            for i in range(level_size):

                if queue[0].left != None:
                    queue.append(queue[0].left)
            
                if queue[0].right != None:
                    queue.append(queue[0].right)
                
                queue.popleft()



    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None:
            return []
        self.max_depth(root)
        return self.output
        