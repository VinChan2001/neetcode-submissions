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
# class Solution:
#     def sortArray(self, nums: List[int]) -> List[int]:
#         for i in range(1,len(nums)):
#             j = i-1
#             current = nums[i]
#             while j>=0 and nums[j]>current:
#                 nums[j+1]=nums[j]
#                 j-=1
#             nums[j+1]=current
#         return nums

#Merge Sort
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        return self.mergeSort(nums)
    def mergeSort(self, nums):
        if len(nums)<=1:
            return nums
        mid = len(nums)//2

        left = self.mergeSort(nums[:mid])
        right = self.mergeSort(nums[mid:])

        return self.merge(left, right)

    def merge(self, l, r):
        result, i, j=[], 0, 0

        while i<len(l) and j<len(r):
            if l[i]<r[j]:
                result.append(l[i])
                i+=1
            else:
                result.append(r[j])
                j+=1
        result.extend(l[i:])
        result.extend(r[j:])
        return result