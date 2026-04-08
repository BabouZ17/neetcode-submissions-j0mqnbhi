class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
            
        rob1 = rob2 = 0

        for i in range(1, len(nums)):
            rob1, rob2 = rob2, max(nums[i] + rob1, rob2)
        best_rob2 = rob2

        rob1 = rob2 = 0
        for i in range(len(nums) - 1):
            rob1, rob2 = rob2, max(nums[i] + rob1, rob2)
        return max(rob2, best_rob2)