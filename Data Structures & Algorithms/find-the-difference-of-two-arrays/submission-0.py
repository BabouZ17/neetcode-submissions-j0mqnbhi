class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        unique_nums1, unique_nums2 = set(nums1), set(nums2)

        return [
            list(unique_nums1 - unique_nums2), 
            list(unique_nums2 - unique_nums1)
        ]