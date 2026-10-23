class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0, len(nums)-1

        def b_s(l, r):
            if l> r:
                return -1
            
            mid = l+(r-l)//2

            if target < nums[mid]:
                return b_s(l, mid-1)
            if target > nums[mid]:
                return b_s(mid+1, r)
            else:
                return mid
        
        return b_s(l, r)
            
        