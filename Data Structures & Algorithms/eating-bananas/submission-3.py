class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def canEat(speed: int) -> bool:
            t = 0
            for p in piles:
                t += math.ceil(p/speed)
            return t <= h

        l, r = 1, max(piles)
        res = r

        while l <= r:
            speed = l + (r-l) // 2
            if canEat(speed):
                res = min(res, speed)
                r = speed - 1
            else:
                l = speed + 1
        return res
