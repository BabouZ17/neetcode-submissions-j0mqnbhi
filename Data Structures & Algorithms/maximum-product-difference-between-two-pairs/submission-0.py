class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        min_pair = min_val = float("inf")
        max_pair = max_val = float("-inf")
        for num in nums:
            min_pair = min(min_pair, min_val * num)
            max_pair = max(max_pair, max_val * num)
            min_val = min(min_val, num)
            max_val = max(max_val, num)
        return max_pair - min_pair