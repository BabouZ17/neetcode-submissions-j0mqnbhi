class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        previous = {num: num for num in nums}

        for i in range(len(nums) + 1):
            if i in previous:
                continue
            else:
                return i
