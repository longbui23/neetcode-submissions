class Solution:
    def trap(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        max_l, max_r = 0, 0
        total_area = 0

        while l <= r: 
            if heights[l] < heights[r]:
                max_l = max(max_l, heights[l])
                total_area += (max_l - heights[l])
                l += 1
            else:
                max_r = max(max_r, heights[r])
                total_area += (max_r - heights[r])
                r -= 1
        
        return total_area


