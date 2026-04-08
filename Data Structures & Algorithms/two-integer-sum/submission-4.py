class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev = dict()
        for i, num in enumerate(nums):
            remainer = target - num
            if remainer in prev.keys():
                return [prev[remainer], i]
            prev[num] = i
        
