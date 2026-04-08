class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        if len(firstList) == 0 or len(secondList) == 0:
            return list()

        res = list()
        for i in range(len(firstList)):
            startA, endA = firstList[i][0], firstList[i][1]
            for j in range(len(secondList)):
                startB, endB = secondList[j][0], secondList[j][1]

                if (startA <= startB <= endA) or (startB <= startA <= endB):
                    res.append([max(startA, startB), min(endA, endB)])
        return res