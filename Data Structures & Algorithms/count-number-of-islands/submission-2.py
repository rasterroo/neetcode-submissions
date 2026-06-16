from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        n, m = len(grid), len(grid[0])
        islands = 0

        def bfs(r, c):
            queue = deque()
            grid[r][c] = "0"
            queue.append((r,c))

            while queue:
                cell = queue.popleft()
                x, y = cell[0], cell[1]
                for dx, dy in directions:
                    nr, nc = x+dx, y+dy
                    if 0<=nr<n and 0<=nc<m and grid[nr][nc]=="1":
                        queue.append((nr, nc))
                        grid[nr][nc] = "0"
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1":
                    islands += 1 
                    bfs(i, j)
        
        return islands

