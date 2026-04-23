class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited = set()
        adj = [[] for _ in range(n)]
        count = 0
       
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            

        def dfs(node):
            for nei in adj[node]:
                if nei not in visited:
                    visited.add(nei)
                    dfs(nei)

        for node in range(n):
            if node not in visited:
                visited.add(node)
                dfs(node)
                count += 1

        return count
