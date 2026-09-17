class Solution:
    def trap(self, height: List[int]) -> int:
        # solution 1
        # water = 0
        # for i in range(len(height)):
        #     leftMax = max(height[:i+1])
        #     rightMax= max(height[i:])

        #     water += min(leftMax, rightMax) - height[i]

        # return water
        l=0
        r=len(height)-1

        leftMax= height[l]
        rightMax= height[r]
        water = 0

        while l<r:
            if leftMax<rightMax:
                l+=1
                leftMax= max(leftMax, height[l])
                water+=leftMax-height[l]
            
            else:
                r-=1
                rightMax = max(rightMax, height[r])
                water+=rightMax-height[r]
        
        return water



       




        
        