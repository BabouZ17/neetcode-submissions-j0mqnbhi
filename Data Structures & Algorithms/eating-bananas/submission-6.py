import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)

        res = r
        while l <= r:
            m = l + (r-l)//2
            if self.canEat(m, h, piles):
                res = min(res, m)
                r = m - 1
            else:
                l = m + 1
        return res

    def canEat(self, speed: int, h: int, piles: list[int]) -> bool:
        total = 0
        for p in piles:
            total += math.ceil(p / speed)
        return total <= h

