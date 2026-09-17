class Solution:
    def calPoints(self, operations: List[str]) -> int:
        s = []
        for i in operations:
            if i == '+':
                s.append(s[-1]+s[-2])
            elif i == 'C':
                s.pop()
            elif i == 'D':
                j = int(s[-1])*2
                s.append(j)
            elif -30000<=int(i)<=30000:
                s.append(int(i))
            
        return sum(s)