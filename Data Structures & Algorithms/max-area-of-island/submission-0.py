class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        def dfs(row, col):
            if row < 0 or row >= ROWS or col < 0 or col >= COLS or grid[row][col] == 0:
                return 0
            
            if (row, col) in visited:
                return 0
            
            visited.add((row, col))
            
            area = 1
            for dr, dc in directions:
                area += dfs(row + dr, col + dc)
            
            return area
        
        ans = 0
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) not in visited and grid[r][c] == 1:
                    islandArea = dfs(r, c)
                    ans = max(ans, islandArea)
        
        return ans