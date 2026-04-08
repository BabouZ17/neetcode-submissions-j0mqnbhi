class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = list()
        nums.sort()
        n = len(nums) - 1

        for i, a in enumerate(nums):
            if a > 0:
                break

            if i > 0 and a == nums[i-1]:
                continue

            l, r = i + 1, n
            while l < r:
                three_sum = a + nums[l] + nums[r]
                if three_sum > 0:
                    r -= 1
                elif three_sum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    r -= 1
                    l += 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
        return res