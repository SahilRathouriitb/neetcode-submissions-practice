class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        graph = self.graph_construct(grid)
        return self.bfs_components(graph)

    def bfs_components(self, graph):
        max_count = 0
        tracker = set()
        for j in graph:
            if j in tracker:
                continue
            count = self.bfs(tracker, j, graph) 
            max_count = max(count, max_count)
        return max_count

    def bfs(self, tracker, node, graph):
        q = deque()
        q.append(node)
        tracker.add(node)
        count = 1
        while len(q) > 0:
            for k in graph[q[0]]:
                if k in tracker:
                    continue
                tracker.add(k)
                count += 1
                q.append(k)

            q.popleft()
        return count




    def graph_construct(self, grid):
        graph = dict()
        for i in range(len(grid)):
            
            for j in range(len(grid[i])):

                if grid[i][j] == 0:
                    continue

                graph[(i,j)] = []

                if i-1 >= 0 and grid[i-1][j] != 0:
                    graph[(i,j)].append((i-1,j))

                if i+1 < len(grid) and grid[i+1][j] != 0:
                    graph[(i,j)].append((i+1, j))
                
                if j+1 < len(grid[0]) and grid[i][j+1] != 0:
                    graph[(i,j)].append((i, j+1))
                
                if j-1 >= 0 and grid[i][j-1] != 0:
                    graph[(i,j)].append((i, j-1))

        return graph
        