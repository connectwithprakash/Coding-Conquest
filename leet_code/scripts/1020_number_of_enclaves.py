class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        def traverse_island(x, y):
            grid[x][y] = 0
            for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                x_new, y_new = x+dx, y+dy
                if (0 <= x_new < m) and (0 <= y_new < n) and (grid[x_new][y_new] == 1):
                    traverse_island(x_new, y_new)

        m, n = len(grid), len(grid[0])
        for x in range(m):
            for y in range(n):
                if (grid[x][y] == 1) and ((x == 0) or (x == (m-1)) or (y == 0) or (y == (n-1))):
                    traverse_island(x, y)
        
        return sum([sum(row) for row in grid])

