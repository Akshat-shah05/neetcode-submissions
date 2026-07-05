class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ROWS, COLS = len(board), len(board[0])
        boxes = defaultdict(set)
        cols = defaultdict(set)

        # Handles Row
        for r in range(ROWS):
            seenRowR = set()
            for c in range(COLS):
                if (board[r][c] in seenRowR or 
                    board[r][c] in boxes[(r//3, c//3)] or
                    board[r][c] in cols[c]):
                    return False
                if board[r][c] != ".":
                    seenRowR.add(board[r][c])
                    boxes[(r//3, c//3)].add(board[r][c])
                    cols[c].add(board[r][c])
        
        return True

        