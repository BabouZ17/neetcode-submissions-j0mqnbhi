class Solution:
    def rob(self, nums: List[int]) -> int:
        def helper(nums: List[int]) -> int:
            rob1, rob2 = 0, 0
            for num in nums:
                tmp = max(num + rob1, rob2)
                rob1 = rob2
                rob2 = tmp
            return rob2
        
        return max(helper(nums[1:]), helper(nums[:-1]), nums[0])