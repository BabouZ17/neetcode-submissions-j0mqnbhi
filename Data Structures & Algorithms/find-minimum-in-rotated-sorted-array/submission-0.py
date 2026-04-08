class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        min_val = float("inf")

        while l<=r:
            middle = l + (r-l)//2
            min_val = min(min_val, nums[middle])
            if nums[middle] > nums[r]:
                l = middle + 1
            else:
                r = middle - 1
        return min(min_val, nums[l])
    
    def rotateArrayFirstItem(self, nums: List[int], k: int) -> List[int]:
        return nums[-k]
    