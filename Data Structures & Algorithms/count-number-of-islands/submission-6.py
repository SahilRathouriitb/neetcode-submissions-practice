class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        graph = self.graph_construct(grid)
        return self.count_components(graph)



    def graph_construct(self, grid):
        graph = dict()
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] != "1":
                    continue
                graph[(i,j)] = []
                # We will check the four neighbors
                if i-1 >= 0 and grid[i-1][j] == "1":
                    graph[(i,j)].append((i-1,j))
                
                if i+1 < len(grid) and grid[i+1][j] == "1":
                    graph[(i,j)].append((i+1,j))
                
                if j-1 >= 0 and grid[i][j-1] == "1":
                    graph[(i,j)].append((i,j-1))

                if j+1 < len(grid[i]) and grid[i][j+1] == "1":
                    graph[(i,j)].append((i,j+1))

        
        return graph 


    def count_components(self,graph):
        count = 0 
        tracker = set()
        for k in graph:
            if k in tracker:
                continue
            count += 1
            self.dfs(graph, k, tracker)
        return count

    def dfs(self, graph, node, tracker):
        for k in graph[node]:
            if k in tracker:
                continue
            tracker.add(k)
            self.dfs(graph, k, tracker)
