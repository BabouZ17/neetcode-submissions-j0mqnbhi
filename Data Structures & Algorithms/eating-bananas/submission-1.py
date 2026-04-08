class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)

        bananas_total = sum(piles)

        res = r
        while l <= r:
            m = l + (r-l)//2
            eating_time = self.eating_time(piles, m)
            if eating_time <= h:
                res = m
                r = m - 1
            else:
                l = m + 1
        return res

    def eating_time(self, piles: List[int], speed: int) -> int:
        eating_time = 0
        for pile in piles:
            eating_time += math.ceil(float(pile) / speed)
        return eating_time