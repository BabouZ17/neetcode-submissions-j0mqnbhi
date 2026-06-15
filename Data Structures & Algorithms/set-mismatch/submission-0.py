class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        seen = set()
        n = len(nums)
        missing = twice = 0
        for num in nums:
            if num in seen:
                twice = num
            seen.add(num)

        for num in range(1, n+1):
            if num not in seen:
                missing = num
        return [twice, missing]
