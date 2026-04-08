class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = currSum = 0
        prefixs = {0: 1}

        for num in nums:
            currSum += num
            diff = currSum - k
            res += prefixs.get(diff, 0)

            prefixs[currSum] = 1 + prefixs.get(currSum, 0)
        return res