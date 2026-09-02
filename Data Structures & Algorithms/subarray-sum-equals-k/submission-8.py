from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = defaultdict(int)
        count[0]=1
        res=0
        prefix = 0

        for i in nums:
            prefix+=i
            if prefix-k in count:
                res+=count[prefix-k]
            count[prefix]+=1
        
        return res

        
        



        