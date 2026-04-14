from collections import Counter

class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        freqs = Counter(nums)
        nums.sort(key=lambda x: (freqs[x], -x))
        return nums
                