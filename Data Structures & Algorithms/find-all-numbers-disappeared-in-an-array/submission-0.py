class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        res = {i for i in range(1, len(nums) + 1)}

        for num in nums:
            res.discard(num)
        return list(res)