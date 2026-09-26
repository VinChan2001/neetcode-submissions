class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = len(board) #[[],[],[]..these]
        cols = len(board[0]) #[[these],[],[]]

        r =  defaultdict(set)
        c = defaultdict(set)

        b = defaultdict(set)

        for i in range(rows):
            for j in range(cols):
                val = board[i][j]

                if val==".":
                    continue
                
                if (
                    val in r[i] or
                    val in c[j] or
                    val in b[(i//3,j//3)]
                ):
                    return False

                r[i].add(val)
                c[j].add(val)
                b[(i//3,j//3)].add(val)

        return True

        