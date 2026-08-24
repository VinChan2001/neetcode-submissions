from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # k most frequent elements
        d1= defaultdict(int)
        for i in nums:
            d1[i]+=1
        
        p=0
        l=[]
        
        while p<k and d1:
            # Reset before every new search
            maxi=0
            maxi_i=-1
            for i, j in d1.items():
                if j>maxi:
                    maxi=j
                    maxi_i=i
            p+=1
            l.append(maxi_i)
            d1.pop(maxi_i)
        return l


            

        