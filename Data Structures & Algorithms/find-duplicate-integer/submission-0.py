class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        previous = {}

        for num in nums:
            if num in previous:
                return num
            previous[num] = num
