class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #optimal solution

        store = set(nums)
        res = 0

        for i in store:
            if i-1 not in store:
                curr = i
                streak = 1
                while curr+1 in store:
                    curr+=1
                    streak+=1
                res = max(res, streak)
        return res
        