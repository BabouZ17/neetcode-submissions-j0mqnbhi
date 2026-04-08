class Solution:
    def rob(self, nums: List[int]) -> int:
        return max(nums[0], self.helper(nums[1:]), self.helper(nums[:-1]))
    
    def helper(self, nums):
        rob1 = rob2 = 0

        for num in nums:
            rob1, rob2 = rob2, max(num + rob1, rob2)
        return rob2

        rob1 = rob2 = 0
        for i in range(len(nums) - 1):
            rob1, rob2 = rob2, max(nums[i] + rob1, rob2)
        return max(rob2, best_rob2)