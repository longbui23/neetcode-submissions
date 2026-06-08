class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        start = 0
        res = []

        for i in range(k-1, len(nums)):
            res.append(max(nums[start:i+1]))
            start += 1

        return res