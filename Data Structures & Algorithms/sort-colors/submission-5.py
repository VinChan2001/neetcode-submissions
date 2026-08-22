class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums[:] = self.mergesort(nums)    
        
    def mergesort(self, nums):
        if len(nums)<=1:
            return nums
        
        mid = len(nums)//2

        left = self.mergesort(nums[:mid])
        right = self.mergesort(nums[mid:])

        return self.merge(left, right)

    def merge(self, l, r):
        i, j, result = 0, 0, []

        while i< len(l) and j<len(r):
            if l[i]<=r[j]:
                result.append(l[i])
                i+=1
            else:
                result.append(r[j])
                j+=1
        result.extend(l[i:])
        result.extend(r[j:])
        return result

