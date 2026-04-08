class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l = 0
        res = list()

        for r in range(len(arr)):
            res.append(arr[r])

            if len(res) > k:
                if abs(arr[r] - x) < abs(res[l] - x):
                    l += 1
        return res[l: l+k]