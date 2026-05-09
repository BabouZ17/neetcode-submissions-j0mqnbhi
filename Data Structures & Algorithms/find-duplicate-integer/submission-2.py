class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums2 = nums[:]
        nums2.sort()

        for i in range(len(nums2)):
            if i > 0 and nums2[i] == nums2[i-1]:
                return nums2[i]
        