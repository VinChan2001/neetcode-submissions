class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        i=0
        k=0
        for i in range(len(nums)):
            if nums[i]!=val:
                nums[k]=nums[i]
                k+=1
            else:
                i+=1
        return k