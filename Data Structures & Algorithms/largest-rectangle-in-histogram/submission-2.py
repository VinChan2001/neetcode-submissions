class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        maxArea = 0

        # Stack stores indices of bars.
        # The heights at these indices stay in increasing order.
        stack = []

        # Go one step beyond the array.
        # i == n acts like a fake bar of height 0
        # so that all remaining bars get popped and processed.
        for i in range(n + 1):

            # Keep popping while:
            # 1. we reached the end, OR
            # 2. current bar is shorter than/equal to stack top bar
            #
            # This means the bar at stack top has found
            # its first smaller bar on the RIGHT.
            while stack and (
                i == n or heights[stack[-1]] >= heights[i]
            ):

                # Pop the bar whose rectangle can no longer continue.
                poppedIndex = stack.pop()
                height = heights[poppedIndex]

                # If stack is empty:
                # there is no smaller bar on the LEFT,
                # so this rectangle can extend from index 0 to i - 1.
                if not stack:
                    width = i

                # Otherwise:
                # current i = first smaller bar on the RIGHT
                # stack[-1] = first smaller bar on the LEFT
                #
                # Usable range is:
                # stack[-1] + 1 ... i - 1
                else:
                    width = i - stack[-1] - 1

                # Calculate rectangle area for this height.
                area = height * width

                # Keep the largest area seen so far.
                maxArea = max(maxArea, area)

            # Push current index after removing all bars
            # that cannot continue through the current height.
            stack.append(i)

        return maxArea