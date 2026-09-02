class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = prefix = 0
        count = defaultdict(int)
        count[0]=1
        for i in nums:
            prefix+=i
            if prefix-k in count:
                res+=count[prefix-k]
            count[prefix]+=1
        return res

        