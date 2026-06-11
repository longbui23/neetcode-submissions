class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        max_area = 0

        while l < r:
            curr_height = min(heights[l], heights[r])
            max_area = max(max_area, curr_height * (r - l))

            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1

        return max_area