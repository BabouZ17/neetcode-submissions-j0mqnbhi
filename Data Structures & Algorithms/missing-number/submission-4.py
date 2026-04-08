class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums = sorted(nums)
        list_of_numbers = [val for val in range(len(nums) + 1)]
        
        for i in range(len(list_of_numbers)):
            if (i>= len(nums)) or i < len(nums) and nums[i] != list_of_numbers[i]:
                return list_of_numbers[i]

