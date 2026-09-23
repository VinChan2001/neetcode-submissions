from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        mp = Counter(nums)
        d={}
        for i, j in mp.items():
            d[j]=i
        
        return d[max(d.keys())]
        