class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevs = dict()
        for i, num in enumerate(nums):
            remainer = target - num
            if remainer in prevs:
                return [prevs[remainer], i]
            prevs[num] = i
    
