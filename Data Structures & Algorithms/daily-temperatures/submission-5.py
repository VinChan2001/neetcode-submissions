class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        temps=[]
        res = [0]*(len(temperatures))

        for i, temp in enumerate(temperatures):
            while temps and temperatures[temps[-1]]<temp:
                prev_i = temps.pop()
                res[prev_i] = i-prev_i

            temps.append(i)

        return res
            

        