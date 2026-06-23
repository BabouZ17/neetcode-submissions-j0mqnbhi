class Solution:
    def largestGoodInteger(self, num: str) -> str:
        res = -1

        i = 1
        while i < len(num) - 1:
            if num[i-1] == num[i] == num[i+1]:
                res = max(res, int(num[i]))
            i += 1
        return "" if res == -1 else str(res) * 3