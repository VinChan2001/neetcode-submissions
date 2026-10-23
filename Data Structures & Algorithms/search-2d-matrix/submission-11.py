class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        def b_s(l,r , nums):
            if l>r :
                return False
            mid = l+ (r-l)//2

            if target<nums[mid]:
                return b_s(l, mid-1, nums)
            if target>nums[mid]:
                return b_s(mid+1, r, nums)
            else:
                return True
        
        for i in range(len(matrix)):
            l,r = 0, len(matrix[i])-1

            if b_s(l, r, matrix[i]):
                return True
        return False
            
            