class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        vals = mat[0]
        for val in mat[0]:
            found = True
            for row in mat[1:]:
                if not self.binary_search(row, val):
                    found = False
                    break
            if found:
                return val
        return -1

    def binary_search(self, vals: list[int], target: int) -> bool:
        l, r = 0, len(vals) - 1
        while l <= r:
            m = l + (r-l)//2
            if vals[m] == target:
                return True
            elif vals[m] > target:
                r = m - 1
            else:
                l = m + 1
        return False