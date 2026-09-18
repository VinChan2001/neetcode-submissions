class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0]*(len(temperatures))
        for i, temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]]< temp:
                prev_i = stack.pop()
                # number of days btw current warm day and prev day
                res[prev_i]= i - prev_i
            stack.append(i)
        
        return res


        