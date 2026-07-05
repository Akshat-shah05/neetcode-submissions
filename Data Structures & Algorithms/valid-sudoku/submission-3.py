class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        SIZE = 9
        rowMap = defaultdict(set)
        colMap = defaultdict(set)
        boxMap = defaultdict(set)

        for r in range(SIZE):
            for c in range(SIZE):
                item = board[r][c]
                if item == ".":
                    continue
                boxRow, boxCol = r // 3, c // 3
                if item in rowMap[r] or item in colMap[c] or item in boxMap[(boxRow, boxCol)]:
                    return False
                
                rowMap[r].add(item)
                colMap[c].add(item)
                boxMap[(boxRow, boxCol)].add(item)
        
        return True

