class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # if not nums:
        #     return 0
        # nums.sort()
        # res = 1
        # streak = 1
        
        # for i in range(1,len(nums)):
        #     if nums[i]==nums[i-1]:
        #         continue
            
        #     if (nums[i]-nums[i-1]) ==1:
        #         streak+=1
            
        #     else:
        #         streak =1
        #     res = max(res, streak)
        # return res

        nums = set(nums)
        res = 0

        for i in nums:
            if i-1 not in nums:
                streak=1
                curr = i
                while curr+1 in nums:
                    curr+=1
                    streak+=1
                res = max(res, streak)
        return res
            
        