class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:

        # Step 1, construction of graph
        graph = dict()
        for i in range(1, n+1):
            graph[i] = []
        
        for k in trust:
            graph[k[0]].append(k[1])

        # Now we need to find such k, who has no neighbor and is everyone's neighbor

        for k in graph:
            if len(graph[k]) > 0:
                continue

            val = True
            for j in graph:
                if j == k:
                    continue 
                
                if k not in graph[j]:
                    val = False
                    break
            
            if val:
                return k
        
        return -1
        