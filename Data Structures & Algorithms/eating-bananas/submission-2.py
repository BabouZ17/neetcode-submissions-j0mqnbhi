class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def canEat(k: int) -> bool:
            eating_time = 0
            for p in piles:
                eating_time += math.ceil(float(p) / k)
            return eating_time <= h
        
        l, r = 1, max(piles)
        res = r
        while l <= r:
            k = l + (r-l)//2
            if canEat(k):
                res = min(res, k)
                r = k - 1
            else:
                l = k + 1
        return res