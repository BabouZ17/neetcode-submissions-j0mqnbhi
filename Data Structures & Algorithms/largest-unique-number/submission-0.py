from collections import defaultdict, OrderedDict

class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        freqs = defaultdict(int)
        for i, num in enumerate(nums):
            freqs[num] += 1

        sorted_map = OrderedDict(sorted(freqs.items(), reverse=True))
        for num, freq in sorted_map.items():
            if freq == 1:
                return num
        return -1