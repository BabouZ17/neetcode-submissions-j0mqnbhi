class Solution:
    def maxScore(self, s: str) -> int:
        n = len(s)

        l_total = [1 if s[0] == "0" else 0]
        for i in range(1, n-1):
            val = l_total[-1]
            val += 1 if s[i] == "0" else 0
            l_total.append(val)

        r_total = [1 if s[-1] == "1" else 0]
        for i in range(n-2, 0, -1):
            val = r_total[-1]
            val += 1 if s[i] == "1" else 0
            r_total.append(val)
        
        r_total = r_total[::-1]

        res = float("-inf")
        for l, r in zip(l_total, r_total):
            res = max(res, l + r)
        return res