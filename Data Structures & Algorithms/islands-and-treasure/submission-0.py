class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        distance = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r, c))
        
        while q:
            for i in range(len(q)):
                r, c = q.popleft()

                for dr, dc in directions:
                    row, col = dr + r, dc + c
                    
                    if (row < 0 or row == ROWS or col < 0 or col == COLS or
                        grid[row][col] == -1 or grid[row][col] != 2147483647):
                        continue
                    
                    grid[row][col] = distance + 1
                    q.append((row, col))
            
            distance += 1

        