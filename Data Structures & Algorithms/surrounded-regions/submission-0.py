class Solution:
    def solve(self, board: List[List[str]]) -> None:
        visited = set()
        ROWS, COLS = len(board), len(board[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def dfs(row, col):
            if row < 0 or row >= ROWS or col < 0 or col >= COLS:
                return 
            
            if (row, col) in visited:
                return 

            if board[row][col] == "X":
                return 
            
            board[row][col] = "T"

            visited.add((row, col))

            for dr, dc in directions:
                nRow, nCol = row + dr, col + dc
                if nRow >= 0 and nRow < ROWS and nCol >= 0 and nCol < COLS:
                    if board[row + dr][col + dc] == "O":
                        dfs(row + dr, col + dc)
        
        for r in range(ROWS):
            dfs(r, 0)
            dfs(r, COLS - 1)
        
        for c in range(COLS):
            dfs(0, c)
            dfs(ROWS - 1, c)
        
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"
                if board[r][c] == "T":
                    board[r][c] = "O"
                
        


        