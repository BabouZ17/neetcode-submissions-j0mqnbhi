class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        previous = {}
        for i in range(len(nums)):
            remainer = target - nums[i]
            if remainer in previous:
                return [previous[remainer], i]
            previous[nums[i]] = i
