class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = curr = 0
        for num in nums:
            if num == 0:
                curr = 0
            else:
                curr += 1
            res = max(res, curr)
        return res