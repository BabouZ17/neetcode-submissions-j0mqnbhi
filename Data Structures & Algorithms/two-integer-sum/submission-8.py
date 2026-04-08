class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        remaining = dict()
        
        for i in range(len(nums)):
            remain = target - nums[i]
            if remain in remaining:
                return [remaining[remain], i]
            remaining[nums[i]] = i
