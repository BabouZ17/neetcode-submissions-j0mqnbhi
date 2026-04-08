class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = currSum = 0
        res = float("inf")

        for r in range(len(nums)):
            currSum += nums[r]

            while currSum >= target:
                currSum -= nums[l]
                res = min(res, r - l + 1)
                l += 1
        return 0 if res == float("inf") else res