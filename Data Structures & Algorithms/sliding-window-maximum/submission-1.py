class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []

        for i in range(k - 1, len(nums)):
            max_num = max(nums[i-k + 1:i + 1])
            res.append(max_num)

        return res