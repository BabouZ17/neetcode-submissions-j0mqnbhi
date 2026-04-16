from collections import defaultdict

class Solution:
    def findLucky(self, arr: List[int]) -> int:
        freqs = defaultdict(int)
        res = float("-inf")

        for num in arr:
            freqs[num] += 1

        for num in freqs.keys():
            if num == freqs[num]:     
                res = max(res, num)
        return res if res != float("-inf") else -1