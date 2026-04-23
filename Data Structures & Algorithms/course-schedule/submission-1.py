class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {i: [] for i in range(numCourses)}
        visited = set()
        for crs, preq in prerequisites:
            adj[crs].append(preq)

        def dfs(crs):
            if crs in visited:
                return False
            if adj[crs] == []:
                return True

            visited.add(crs)
            for preq in adj[crs]:
                if not dfs(preq):
                    return False
            
            visited.remove(crs)
            adj[crs] = []
            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return False

        return True