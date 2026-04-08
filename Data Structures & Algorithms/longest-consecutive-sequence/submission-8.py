class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        nums = list(set(nums))
        nums.sort()
        currentResult = 0
        result = 0
        prev = 0

        for i in range(len(nums)):
            if nums[i] - prev != 1 and i > 0:
                currentResult = 1
            else:
                currentResult += 1
            prev = nums[i]
            result = max(result, currentResult)
        return result
