class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ROWS, COLS = len(board), len(board[0])
        boxes = defaultdict(set)

        for r in range(ROWS):
            seenRowR = set()
            for c in range(COLS):
                if board[r][c] in seenRowR or board[r][c] in boxes[(r//3, c//3)]:
                    return False
                if board[r][c] != ".":
                    seenRowR.add(board[r][c])
                    boxes[(r//3, c//3)].add(board[r][c])
            
        for c in range(COLS):
            seenColC = set()
            for r in range(ROWS):
                if board[r][c] in seenColC:
                    return False
                if board[r][c] != ".":
                    seenColC.add(board[r][c])
            
            print(seenColC)
        
        return True

        