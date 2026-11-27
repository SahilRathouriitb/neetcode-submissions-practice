"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node == None:
            return None
        store = dict()
        tracker = set()
        seen = set()

        store[node.val] = Node(node.val)
        
        q = deque()
        q.append(node)
        seen.add(node)
        
        while len(q) > 0:

            for k in q[0].neighbors:

                if (k.val, q[0].val) in tracker:
                    continue
                
                if k not in seen:
                    q.append(k)
                    seen.add(k)
                    store[k.val] = Node(k.val)

                tracker.add((q[0].val,k.val))
                
                store[q[0].val].neighbors.append(store[k.val])
                store[k.val].neighbors.append(store[q[0].val])

            
            temp = q.popleft()
            seen.remove(temp)

        return store[1]

