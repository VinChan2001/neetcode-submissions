class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0]*len(temperatures)

        for i in range(len(temperatures)):
            while stack and temperatures[stack[-1]]<temperatures[i]:#curr temp is high than older
                prev_i = stack.pop() #older cold one !
                gap = i - prev_i # gap btw new warm and older cold
                res[prev_i]=gap # telling how long we wait for warm day at that old days location
            stack.append(i)

        return res
        