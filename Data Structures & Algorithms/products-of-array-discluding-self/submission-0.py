class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        zeroes_count = 0
        total_product = 1

        for i in range(len(nums)):
            if nums[i] != 0:
                total_product *= nums[i]
            else:
                zeroes_count += 1

        for i in range(len(nums)):
            if nums[i] != 0 and zeroes_count == 0:
                result.append(total_product // nums[i])
            if nums[i] != 0 and zeroes_count != 0:
                result.append(0)
            if nums[i] == 0 and zeroes_count > 1:
                result.append(0)
            if nums[i] == 0 and zeroes_count == 1:
                result.append(total_product)
        return result
        