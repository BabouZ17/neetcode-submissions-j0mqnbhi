class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        return [self.binary_search(nums, target, True), self.binary_search(nums, target, False)]

    def binary_search(self, nums: List[int], target: int, leftBias: bool) -> int:
        l, r = 0, len(nums) - 1
        i = -1
        while l <= r:
            m = l + (r-l)//2
            if nums[m] > target:
                r = m - 1
            elif nums[m] < target:
                l = m + 1
            else:
                i = m
                if leftBias:
                    r = m - 1
                else:
                    l = m + 1
        return i
