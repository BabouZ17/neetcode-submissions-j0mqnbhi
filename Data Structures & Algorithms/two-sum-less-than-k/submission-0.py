class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        nums.sort()
        l, r = 0, len(nums) - 1
        res = -1

        while l < r:
            if nums[l] + nums[r] >= k:
                r -= 1
            elif nums[l] + nums[r] < k:
                res = max(res, nums[l] + nums[r])
                l += 1
        return res