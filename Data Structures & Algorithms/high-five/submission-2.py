import heapq
from collections import defaultdict

class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        scores = defaultdict(list)
        k = 5

        for item in items:
            student_id, score = item[0], item[1]
            heapq.heappush(scores[student_id], score)

            if len(scores[student_id]) > k:
                heapq.heappop(scores[student_id])

        solution = []
        for student_id in sorted(scores.keys()):
            total = sum(scores[student_id])
            solution.append([student_id, total // k])
        return solution