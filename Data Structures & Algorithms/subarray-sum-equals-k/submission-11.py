class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        prefix = 0

        count = defaultdict(int)
        count[0]=1

        for i in nums:

            #total from the beginning to here
            prefix+=i

            #what previous total do I need
            #to chop off to leave exactly k
            old_prefix=prefix-k

            #how many times did that old_total occur?
            if old_prefix in count:
                res+=count[old_prefix]

            #remember current total for the future
            count[prefix]+=1
        return res
        