class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev = dict()
        for i, num in enumerate(nums):
            remainer = target - num
            print(remainer, prev)
            if remainer in prev:
                return [prev[remainer], i]
            prev[num] = i
        