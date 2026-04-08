class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums is None or len(nums) == 0:
            return 0

        res = 0
        maxLength = 1
        nums = sorted(set(nums))
        for i in range(1, len(nums)):
            if nums[i] - nums[i-1] == 1:
                maxLength += 1
            else:
                res = max(res, maxLength)
                maxLength = 1
        return max(res, maxLength)