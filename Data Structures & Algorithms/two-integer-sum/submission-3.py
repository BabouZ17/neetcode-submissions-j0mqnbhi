class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev = {}
        for i, num in enumerate(nums):
            remaining = target - num
            if remaining in prev:
                return [prev[remaining], i]
            else:
                prev[num] = i
            