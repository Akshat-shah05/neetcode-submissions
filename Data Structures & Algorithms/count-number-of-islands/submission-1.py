class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid)
        m = len(grid[0])

        visited = set()
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        def dfs(row, col):
            if row < 0 or row >= n or col < 0 or col >= m or grid[row][col] == "0":
                return 
            
            if (row, col) in visited:
                return
            
            visited.add((row, col))
            
            for x, y in directions:
                dfs(row + x, col + y)
            
            return 
        
        ans = 0
        for i in range(n): 
            for j in range(m):
                if (i, j) not in visited and grid[i][j] == "1": 
                    dfs(i, j)
                    ans += 1
        
        return ans