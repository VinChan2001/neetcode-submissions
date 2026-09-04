class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        count = [0]*3
        for i in nums:
            count[i]+=1
        
        i=0
        j=0
        while j<len(nums):
            k=0
            while k<count[i]:
                nums[j]=i
                j+=1
                k+=1
            i+=1
        return nums


