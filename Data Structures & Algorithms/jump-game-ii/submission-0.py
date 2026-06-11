class Solution:
    def jump(self, nums: List[int]) -> int:
        curr_far, curr_end = 0, 0
        res = 0

        for i in range(len(nums) - 1):
            curr_far = max(i + nums[i], curr_far)
            if i == curr_end:
                res += 1
                curr_end = curr_far

        return res

        