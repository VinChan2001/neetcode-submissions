class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        rmax = -1
        n = len(arr)
        ans = [0]*n

        for i in range(n-1, -1, -1):

            ans[i] = rmax
            rmax = max(arr[i], rmax)

        return ans

        