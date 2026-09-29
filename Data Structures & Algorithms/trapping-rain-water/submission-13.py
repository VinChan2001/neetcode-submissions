class Solution:
    def trap(self, height: List[int]) -> int:
        l=0
        r = len(height)-1

        leftM = height[l]
        rightM = height[r]
        water = 0

        while l<r:
            if leftM < rightM:

                l+=1
                leftM = max(leftM, height[l])
                water+=leftM-height[l]

            else:
                r-=1
                rightM = max(rightM, height[r])
                water+=rightM-height[r]

        return water
        