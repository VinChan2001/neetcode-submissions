class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count=0
        k=[0]
        for i in range(len(nums)):
            if nums[i] == 1:
                count+=1
                k.append(count)
            elif nums[i]==0:
                k.append(count)
                count=0

        return max(k)