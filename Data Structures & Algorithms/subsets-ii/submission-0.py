class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = list()
        subset = list()

        nums.sort()

        def backtrack(i: int):
            if i == len(nums):
                res.append(subset.copy())
                return

            subset.append(nums[i])
            backtrack(i + 1)
            subset.pop()

            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            backtrack(i + 1)            

        backtrack(0)
        return res