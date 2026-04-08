class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        prevs = set()
        for num in nums:
            if num in prevs:
                return True
            prevs.add(num)
        return False