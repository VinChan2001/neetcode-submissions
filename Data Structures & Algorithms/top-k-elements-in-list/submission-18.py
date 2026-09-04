from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # counter = defaultdict(int)

        # for i in nums:
        #     counter[i]+=1
        
        # l=[]
        # p=0
        # while p<k:
        #     maxx=0
        #     maxx_i=-1
        #     for i, j in counter.items():
        #         if j>maxx:
        #             maxx=j
        #             maxx_i=i
        #     l.append(maxx_i)
        #     counter.pop(maxx_i)
        #     p+=1
        # return l

        #optimal solution
        d = defaultdict(int)

        for i in nums:
            d[i]+=1
        
        freq=[[] for _ in range(len(nums)+1)]
        for i, j in d.items():
            freq[j].append(i)
        
        res = []
        for i in range(len(freq)-1, -1, -1):
            for num in freq[i]:
                res.append(num)
            if len(res)==k:
                return res





        