from collections import defaultdict

class TimeMap:

    def __init__(self):
        self.vals = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.vals[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.vals:
            return ""

        vals = self.vals[key]
        l, r = 0, len(vals) - 1
        res = ""
        while l <= r:
            m = l + (r-l)//2
            if vals[m][1] <= timestamp:
                res = vals[m][0]
                l = m + 1
            else:
                r = m - 1
        return res