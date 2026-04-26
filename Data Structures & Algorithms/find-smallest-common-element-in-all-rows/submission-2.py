from collections import defaultdict
class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        counts = defaultdict(int)

        for row in mat:
            for val in set(row):
                counts[val] += 1
                if counts[val] == len(mat):
                    return val
        return -1