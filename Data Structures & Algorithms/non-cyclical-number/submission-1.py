class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            n = self.compute(n)
        return n == 1

    def compute(self, n: int) -> int:
        res = 0
        for digit in str(n):
            res += int(digit) * int(digit)
        return res