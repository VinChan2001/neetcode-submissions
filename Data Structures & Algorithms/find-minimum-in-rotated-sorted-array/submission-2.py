class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        l , r = 0, len(nums)-1

        while l<=r:
            #means the array is sorted and you can just get the least at the left
            if nums[l]<nums[r]:
                res = min(res, nums[l])
                break
            
            m = (l+r)//2
            res = min(res, nums[m])
            if nums[m]>=nums[l]: # m @left & is sorted search the right
                l = m+1
            else:
                r = m-1 #m is in right sorted part search left
            
        return res

            
        