class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        nums.sort()

        l, r = 0, len(nums) - 1
        while l <= r:
            m = l + (r-l)//2

            if nums[m] == target:
                return True

            elif target > nums[m]:
                l = m + 1
            else:
                r = m - 1
        return False