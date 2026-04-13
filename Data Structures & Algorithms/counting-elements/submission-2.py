
class Solution:
    def countElements(self, arr: List[int]) -> int:
        res = 0
        unique_values = set(arr)

        for num in arr:
            if num+1 in unique_values:
                res += 1
        return res