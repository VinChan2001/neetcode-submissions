class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        n = len(heights)
        maxArea = 0


        for i in range(n+1):
            while stack and (i==n or heights[stack[-1]]>=heights[i]):
                prev_height = heights[stack.pop()]
                width = i if not stack else i-stack[-1]-1
                maxArea = max(maxArea, width*prev_height)

            stack.append(i)

        return maxArea

        