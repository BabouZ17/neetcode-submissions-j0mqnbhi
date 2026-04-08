class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = curr = 0
        for num in nums:
            if num == 0:
                res = max(res, curr)
                curr = 0
            else:
                curr += 1
        return max(curr, res)