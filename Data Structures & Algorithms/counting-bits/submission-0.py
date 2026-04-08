class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0] * (n + 1)
        for i in range(len(res)):
            res[i] = self.countBitsInNumber(i)
        return res

    def countBitsInNumber(self, n: int) -> int:
        count = 0
        while n:
            n &= n - 1
            count += 1
        return count