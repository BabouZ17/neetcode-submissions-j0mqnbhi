from collections import Counter
class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        counts = Counter(arr)

        for s in arr:
            if counts[s] == 1:
                k -= 1
                if not k:
                    return s
        return ""