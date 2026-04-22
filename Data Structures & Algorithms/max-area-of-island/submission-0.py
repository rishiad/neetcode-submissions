class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_r, max_c = len(grid), len(grid[0])
        visited = set()
        res = 0

        def dfs(r, c):
            if (min(r,c) < 0 or 
                r == max_r or c == max_c or 
                (r,c) in visited or 
                grid[r][c] == 0):
                return 0

            visited.add((r,c))
            count = 1
            count += dfs(r+1, c)
            count += dfs(r-1, c)
            count += dfs(r, c+1)
            count += dfs(r, c-1)

            return count

        for i in range(max_r):
            for j in range(max_c):
                if grid[i][j] == 1 and (i,j) not in visited:
                    res = max(res, dfs(i, j))

        return res
 