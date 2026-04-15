import heapq
from collections import defaultdict

class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        students = defaultdict(list)
        studentsBestAvg = defaultdict(list)

        for studentId, grade in items:
            students[studentId].append(grade)

        for studentId, grades in students.items():
            heapq.heapify(grades)
            while len(grades) > 5:
                heapq.heappop(grades)
            studentsBestAvg[studentId] = grades

        sorted_values = dict(sorted(studentsBestAvg.items(), key=lambda x: x[0]))

        return [[student, sum(grades)//5] for student, grades in sorted_values.items()]