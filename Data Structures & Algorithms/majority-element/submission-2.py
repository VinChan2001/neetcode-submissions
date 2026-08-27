class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d={}
        for i in range(len(nums)):
            d[nums[i]] = d.get(nums[i], 0)+1
        
        for j in range(len(nums)):
            if d[nums[j]] > len(nums)//2:
                return nums[j]