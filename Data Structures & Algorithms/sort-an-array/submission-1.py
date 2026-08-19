#Selection sort
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        for i in range(len(nums)-1):
            mini = i
            for j in range(i, len(nums)):
                if nums[j]< nums[mini]:
                    mini = j
            if mini!= i:
                nums[i], nums[mini] = nums[mini], nums[i]
        return nums