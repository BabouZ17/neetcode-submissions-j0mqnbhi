class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        remainers = {}
        for index, num in enumerate(nums):
            remainer = target - num
            if remainer in remainers.keys():
                return [remainers[remainer], index]
            remainers.update({num: index})
        