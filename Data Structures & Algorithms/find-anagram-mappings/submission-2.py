class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = [0] * len(nums1)

        vals_to_indexes = dict()
        for i in range(len(nums2)):
            vals_to_indexes[nums2[i]] = i

        for i in range(len(nums1)):
            res[i] = vals_to_indexes[nums1[i]]

        return res