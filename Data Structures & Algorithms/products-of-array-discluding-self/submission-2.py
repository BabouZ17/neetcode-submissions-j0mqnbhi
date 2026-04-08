class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result, left_prefix, right_prefix = list(), [1 for num in nums], [1 for num in nums]
        
        total = 1
        for i in range(len(nums)):
            total *= nums[i]
            left_prefix[i] = total

        total = 1
        for i in range(len(nums)-1, -1, -1):
            total *= nums[i]
            right_prefix[i] = total
        
        for i in range(len(nums)):
            left = left_prefix[i-1] if i > 0 else 1
            right = right_prefix[i+1] if i < len(nums) - 1 else 1
            result.append(left * right)
        return result
        