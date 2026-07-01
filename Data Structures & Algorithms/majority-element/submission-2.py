from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        c = Counter(nums)

        for key, cnt in c.items():
            if cnt > len(nums) / 2:
                return key
            