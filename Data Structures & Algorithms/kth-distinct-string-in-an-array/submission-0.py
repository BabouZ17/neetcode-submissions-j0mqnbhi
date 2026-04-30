from collections import defaultdict, Counter

class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        freqs = Counter(arr)
        distincts = list()

        for s in arr:
            if freqs[s] == 1:
                distincts.append(s)

        return distincts[k-1] if len(distincts) >= k  else ""
