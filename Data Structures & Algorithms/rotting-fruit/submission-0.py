class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        time, freshOranges = 0, 0
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    freshOranges += 1
                
                elif grid[r][c] == 2:
                    q.append((r, c))
        
        while q and freshOranges > 0:
            for i in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    row, col = dr + r, dc + c

                    if (row < 0 or col < 0 or
                        row == ROWS or col == COLS or
                        grid[row][col] == 2 or grid[row][col] == 0):
                        continue
                    
                    grid[row][col] = 2
                    q.append((row, col))
                    freshOranges -= 1
            
            time += 1
        
        return time if freshOranges == 0 else -1



        