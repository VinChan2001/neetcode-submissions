class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #sol:1 spc:O(n) time:O(n)
        # n = len(nums)
        # left = [1]*n
        # right = [1]*n
        # ans = [1]*n

        # for i in range(1, n):
        #     left[i] = left[i-1]*nums[i-1]
        # for i in range(n-2, -1, -1):
        #     right[i]= right[i+1]*nums[i+1]
        # for i in range(n):
        #     ans[i]=left[i]*right[i]

        # return ans

        #optimal solution
        ans = [1]* len(nums)

        for i in range(1,len(nums)):
            ans[i]=ans[i-1]*nums[i-1]
        right = 1
        for i in range(len(nums)-1, -1, -1):
            ans[i]*=right
            right*=nums[i]
        return ans