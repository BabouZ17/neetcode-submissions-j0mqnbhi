class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        total = int((n * (n+1)) / 2)

        res = total
        for i in range(n):
            res -= nums[i]
        return res