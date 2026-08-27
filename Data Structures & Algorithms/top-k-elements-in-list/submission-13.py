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

        ## rather than searching here sort it using .sort() then you can simply
        ## top elements the key is to sort the dictionary as you cant sort the keys of a dictionary just sort the list[[k,v]] then take the top k
                

