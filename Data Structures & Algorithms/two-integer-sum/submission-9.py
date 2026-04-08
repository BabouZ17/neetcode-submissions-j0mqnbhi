class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        remaining = dict()
        
        for i, num in enumerate(nums):
            remain = target - num
            if remain in remaining:
                return [remaining[remain], i]
            remaining[num] = i
