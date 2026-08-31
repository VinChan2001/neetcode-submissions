from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        d1 = defaultdict(int)
        rows = len(board)
        cols = len(board[0])

        for i in range(rows):
            for j in board[i]:
                d1[j]+=1
            d1.pop(".", None)
            for v in list(d1.values()):
                if v>1:
                    return False
            d1 = defaultdict(int)
            
        for i in range(rows):
            for j in range(cols):
                d1[board[j][i]]+=1
            d1.pop(".", None)
            for v in list(d1.values()):
                if v>1:
                    return False
            d1 = defaultdict(int)

        p=0
        q=0
        while p<=6:
            sub=[]
            while q<=6:
                for i in range(p,p+3):
                    if q!=6:
                        print(i,q)
                        sub+=board[i][q:q+3]
                        print(sub)
                    else:
                        print(i,q)
                        sub+=board[i][q:q+4]
                        print(sub)
                
                for i in sub:
                    d1[i]+=1
                d1.pop(".", None)
                for v in list(d1.values()):
                        if v>1:
                            return False
                d1 = defaultdict(int)
                q+=3
                sub=[]
            q=0
            p+=3
        return True

            

        

        
        
            

        
            
            


        