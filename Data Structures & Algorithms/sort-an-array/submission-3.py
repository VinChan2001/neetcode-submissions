#Selection sort
# class Solution:
#     def sortArray(self, nums: List[int]) -> List[int]:
        
#         for i in range(len(nums)-1):
#             mini = i
#             for j in range(i, len(nums)):
#                 if nums[j]< nums[mini]:
#                     mini = j
#             if mini!= i:
#                 nums[i], nums[mini] = nums[mini], nums[i]
#         return nums

#Bubble sort
# class Solution:
#     def sortArray(self, nums: List[int]) -> List[int]:
#         for i in range(len(nums)):
#             for j in range(len(nums)-i-1):
#                 if nums[j]>nums[j+1]:
#                     nums[j], nums[j+1] = nums[j+1], nums[j]

        # return nums

#Insertion sort
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        for i in range(1,len(nums)):
            j = i-1
            current = nums[i]
            while j>=0 and nums[j]>current:
                nums[j+1]=nums[j]
                j-=1
            nums[j+1]=current
        return nums

