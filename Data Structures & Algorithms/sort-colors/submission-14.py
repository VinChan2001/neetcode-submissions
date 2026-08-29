class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = [0]*3
        for i in nums:
            count[i]+=1

        j=0
        for i in range(len(count)):
            p=0
            while p<count[i]:
                nums[j]=i
                p+=1
                j+=1




        