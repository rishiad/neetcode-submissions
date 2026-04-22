class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        max_r, max_c = len(grid), len(grid[0])
        visited = set()
        count = 0

        def dfs(r, c):
            if min(r, c) < 0 or r == max_r or c == max_c or (r, c) in visited or grid[r][c] == '0':
                return

            visited.add((r,c))

            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)

        for i in range(max_r):
            for j in range(max_c):
                if grid[i][j] == '1' and (i, j) not in visited:
                    dfs(i, j)
                    count += 1

        return count