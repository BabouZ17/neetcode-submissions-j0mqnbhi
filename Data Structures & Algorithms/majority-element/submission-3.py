from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)

        c = Counter(nums)
        for key, val in c.items():
            if val > n / 2:
                return key
        return -1