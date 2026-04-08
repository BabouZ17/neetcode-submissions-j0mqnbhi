from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.vals = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.vals[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if not self.vals[key]: return ""

        res = ""
        l, r = 0, len(self.vals[key]) - 1
        while l <= r:
            m = l + (r-l)//2
            if self.vals[key][m][1] <= timestamp:
                res = self.vals[key][m][0]
                l = m + 1
            else:
                r = m - 1
        return res
