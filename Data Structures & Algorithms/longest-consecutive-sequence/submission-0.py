class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest_consecutive = 0
        numsSet = set(nums)

        for num in numsSet:
            if (num - 1) not in numsSet:
                length = 1
                while (num + length) in numsSet:
                    length += 1
                longest_consecutive = max(longest_consecutive, length)
        return longest_consecutive