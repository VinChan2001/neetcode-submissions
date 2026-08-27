from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d=defaultdict(int)
        for i in nums:
            d[i]+=1
        j=0
        l=[]
        while j<k and d:
            maxx = 0
            maxx_i = -1
            for ke, f in d.items():
                if f>maxx:
                    maxx=f
                    maxx_i=ke
            l.append(maxx_i)
            d.pop(maxx_i)
            j+=1
        return l
                

