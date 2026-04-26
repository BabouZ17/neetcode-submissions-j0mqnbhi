import heapq
from collections import defaultdict

class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        counts = defaultdict(int)

        for r in range(len(mat)):
            for c in range(len(mat[0])):
                counts[mat[r][c]] += 1

        
        heap = []
        for key, count in counts.items():
            heapq.heappush(heap, (key, count))

        while heap:
            key, count = heapq.heappop(heap)
            if count == len(mat):
                return key
        return -1