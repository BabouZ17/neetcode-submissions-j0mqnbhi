from collections import defaultdict, Counter

class Solution:
    def findLucky(self, arr: List[int]) -> int:
        freqs = defaultdict(int)
        res = float("-inf")

        freqs = Counter(arr)

        for num in freqs.keys():
            if num == freqs[num]:     
                res = max(res, num)
        return res if res != float("-inf") else -1