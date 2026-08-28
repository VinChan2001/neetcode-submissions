import random
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.quick(nums, 0, len(nums)-1)
        return nums
    def quick(self, nums, low, high):
        if low>=high:
            return
        
        pivot_index = self.partition(nums, low, high)

        self.quick(nums, low, pivot_index-1)
        self.quick(nums, pivot_index+1, high)
    def partition(self, nums, low, high):
        
        pivot_index = random.randint(low, high)
        nums[pivot_index], nums[high] = nums[high], nums[pivot_index]

        pivot = nums[high]

        i = low

        for j in range(low, high):
            if nums[j]<pivot:
                nums[i], nums[j] = nums[j], nums[i]
                i+=1
        nums[i], nums[high] = nums[high], nums[i]
        return i

        