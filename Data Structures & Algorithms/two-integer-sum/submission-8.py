from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mp=defaultdict(int)
        for i,j in enumerate(nums):
            diff = target-j
            if diff in mp:
                return [mp[diff],i]
            mp[j]=i
            
        