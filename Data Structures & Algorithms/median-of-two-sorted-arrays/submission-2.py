class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        A, B = nums1, nums2

        # Always binary search the smaller array
        if len(A) > len(B):
            A, B = B, A

        total = len(A) + len(B)
        half = total // 2

        l, r = 0, len(A)

        while l <= r:
            # How many elements to take from A
            cutA = (l + r) // 2

            # Remaining elements must come from B
            cutB = half - cutA

            # Values surrounding both cuts
            LA = A[cutA - 1] if cutA > 0 else float("-inf")
            RA = A[cutA] if cutA < len(A) else float("inf")

            LB = B[cutB - 1] if cutB > 0 else float("-inf")
            RB = B[cutB] if cutB < len(B) else float("inf")

            if LA <= RB and LB <= RA:
                # Correct partition
                if total % 2:
                    return min(RA, RB)

                return (max(LA, LB) + min(RA, RB)) / 2

            elif LA > RB:
                r = cutA - 1

            else:
                l = cutA + 1
            