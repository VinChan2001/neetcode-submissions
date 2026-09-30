class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0]*len(temperatures)

        for i in range(len(temperatures)):
            while stack and temperatures[i]>temperatures[stack[-1]]:
                prev_i = stack.pop() #where current cold temp is 
                res[prev_i] = i-prev_i #how far is that from the current warm temp
            
            stack.append(i)

        return res

        