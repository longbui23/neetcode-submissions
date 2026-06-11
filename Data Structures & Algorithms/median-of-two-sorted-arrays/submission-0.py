class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A,B = nums1, nums2
        if len(A) > len(B):
            A, B = B, A
        m, n = len(A), len(B)
        i, j = 0, m
        half = (m + n + 1) // 2

        while i <= j:
            mid1 = (i + j) // 2
            mid2 = half - mid1

            Aleft = A[mid1 - 1] if mid1 > 0 else float('-inf')
            Aright = A[mid1] if mid1 < m else float('inf')
            Bleft = B[mid2 - 1] if mid2 > 0 else float('-inf')
            Bright = B[mid2] if mid2 < n else float('inf')

            if Aleft <= Bright and Bleft <= Aright:
                if (m + n) % 2 == 0:
                    return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
                else:
                    return max(Aleft, Bleft)
            elif Aleft > Bright:
                j = mid1 - 1
            else:
                i = mid1 + 1