from collections import defaultdict
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        freqs = defaultdict(int)
        l = 0

        for r in range(len(nums)):
            if freqs[nums[r]] < 2:
                nums[l] = nums[r]
                l += 1
                freqs[nums[r]] += 1
        return l