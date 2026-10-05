class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        stack = []
        maxArea = 0
        
        for i in range(n+1):
            while stack and (i==n or heights[stack[-1]] >= heights[i]):
                poppedIndex = stack.pop()
                height = heights[poppedIndex]

                width = i if not stack else i-stack[-1]-1

                area = height*width
                maxArea = max(maxArea, area)

            stack.append(i)
        return maxArea

    




