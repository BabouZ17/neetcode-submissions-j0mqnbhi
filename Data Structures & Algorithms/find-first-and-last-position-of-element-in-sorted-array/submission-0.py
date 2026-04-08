class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)

        def binary_search(target: int) -> int:
            l, r = 0, n
            while l < r:
                m = l + (r-l)//2
                if nums[m] >= target:
                    r = m
                else:
                    l = m + 1
            return l
        
        start = binary_search(target)
        if start == n or nums[start] != target:
            return [-1, -1]
        return [start, binary_search(target + 1) - 1]
