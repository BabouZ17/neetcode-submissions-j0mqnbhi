from collections import defaultdict

class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((value, timestamp))

    def findValue(self, values: list, timestamp: int) -> str:
        l, r = 0, len(values) - 1
        res = ""

        while l <= r:
            m = l + (r-l)//2
            if values[m][1] <= timestamp:
                res = values[m][0]
                l = m + 1
            else:
                r = m - 1
        return res

    def get(self, key: str, timestamp: int) -> str:
        if key in self.store:
            return self.findValue(self.store[key], timestamp)
        return ""
