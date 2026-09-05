from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        r = len(board)
        c = len(board[0])

        rows = defaultdict(set)
        cols = defaultdict(set)

        boxs = defaultdict(set)

        for i in range(r):
            for j in range(c):
                val = board[i][j]

                if val==".":
                    continue

                if (val in rows[i] or 
                    val in cols[j] or
                    val in boxs[(i//3,j//3)]):
                    return False
                
                rows[i].add(val)
                cols[j].add(val)
                boxs[(i//3,j//3)].add(val)

        return True
        