class Solution:
    def search(self, nums: List[int], target: int) -> int:

        l, r = 0, len(nums)-1
        
        while l<=r:

            m = (l+r)//2

            if nums[m]==target:
                return m
            
            if nums[m]<=nums[r]: #right part is sorted
                if nums[m]<=target<=nums[r]: #target in the sorted part
                    l = m+1
                else:
                    r = m-1
            else: #left part is sorted
                if nums[l]<=target<=nums[m]:#target in the sorted part
                    r = m-1
                else:
                    l = m+1

        return -1
            
        