class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # l, r = 0, len(nums)-1
        

        # while l<=r:
        #     mid = l+((r-l)//2)

        #     if target<nums[mid]:
        #         r=mid-1
        #     elif target>nums[mid]:
        #         l=mid+1
        #     else:
        #         return mid
        
        # return -1
        
        def binary_search(l, r):
            # Stop when the search range is empty.
            if l > r:
                return -1

            mid = (l + r) // 2

            if target < nums[mid]:
                return binary_search(l, mid - 1)

            if target > nums[mid]:
                return binary_search(mid + 1, r)

            return mid

        return binary_search(0, len(nums) - 1)