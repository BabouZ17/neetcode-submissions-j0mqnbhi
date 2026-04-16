from collections import defaultdict, Counter

class Solution:
    def findLucky(self, arr: List[int]) -> int:
        freqs = Counter(arr)
        res = float("-inf")

        return max([num for num, count in freqs.items() if num == count], default=-1)