class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        duplicates = {}
        for num in nums:
            if num in duplicates.keys():
                return True
            
            duplicates.update({num: 1})
        return False