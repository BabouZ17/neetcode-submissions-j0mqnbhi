class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n not in seen:
            seen.add(n)
            n = self.compute(n)
            if n == 1:
                return True
        return False

    def compute(self, n: int) -> int:
        res = 0
        while n:
            digit = n % 10
            res += digit ** 2
            n //= 10
        return res