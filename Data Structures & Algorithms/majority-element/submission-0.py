from collections import defaultdict

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = defaultdict(int)

        for num in nums:
            counter[num] += 1
        
        for key, cnt in counter.items():
            if cnt > len(nums) / 2:
                return key
        