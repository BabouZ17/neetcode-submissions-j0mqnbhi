class Solution:

    def binary_search(self, nums: List[int], target:int) -> int:
        l,r = 0, len(nums) -1

        while l <= r:
            middle = l + (r-l) // 2

            if target > nums[middle]:
                l = middle + 1
            elif target < nums[middle]:
                r = middle - 1
            else:
                return middle
        return -1

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i, row in enumerate(matrix):
            if row[-1] < target:
                continue

            if self.binary_search(nums=[val for val in row], target=target) != -1:
                return True
        return False