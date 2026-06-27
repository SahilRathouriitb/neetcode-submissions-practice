# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        output = []
        q = deque([root])
        l = 0

        while len(q) > 0:
            l = len(q)
            output.append(q[-1].val)
            for i in range(l):
                if q[0].left:
                    q.append(q[0].left)
                if q[0].right:
                    q.append(q[0].right)
                q.popleft()
        return output
                

        