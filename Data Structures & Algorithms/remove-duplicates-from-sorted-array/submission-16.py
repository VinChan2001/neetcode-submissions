class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l1= 0
        r=len(nums)-1
        while l1<r:
            l2=l1+1
            while l2<r:
                if nums[l1]==nums[l2]:
                    nums.remove(nums[l2])
                    r=len(nums)-1
                else:
                    l2+=1
            if nums[l1]==nums[r]:
                nums.remove(nums[l1])
                r=len(nums)-1
            l1+=1
        
        return len(nums)
            

        
            

        