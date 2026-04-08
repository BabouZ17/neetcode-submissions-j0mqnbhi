class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r

        while l <= r:
            m = l + (r-l)//2
            if self.canEat(piles, m, h):
                res = min(res, m)
                r = m - 1
            else:
                l = m + 1
    
        return res

    def canEat(self, piles: list[int], speed: int, h: int) -> bool:
        time = 0
        for p in piles:
            time += math.ceil(p / speed)
        return time <= h
