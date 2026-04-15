from collections import defaultdict

class Solution:
    def maxDifference(self, s: str) -> int:
        freqs = defaultdict(int)
        for char in s:
            freqs[char] += 1

        max_odd, min_even = float("-inf"), float("inf")
        for freq in freqs.values():
            # odd
            if freq % 2:
                max_odd = max(max_odd, freq)
            # even
            else:
                min_even = min(min_even, freq)

        return max_odd - min_even