from collections import defaultdict

class Solution:
    def countElements(self, arr: List[int]) -> int:
        res = 0
        freqs = defaultdict(int)

        for num in arr:
            freqs[num] += 1

        for num in arr:
            if freqs[num+1]:
                res += 1
        return res