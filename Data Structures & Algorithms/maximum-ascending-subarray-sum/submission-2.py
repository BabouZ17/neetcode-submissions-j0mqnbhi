class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        currSum = nums[0]
        res = currSum
        for i in range(1, len(nums)):
            if nums[i-1] >= nums[i]:
                currSum = nums[i]
            else:
                currSum += nums[i]
            res = max(res, currSum)
        return res