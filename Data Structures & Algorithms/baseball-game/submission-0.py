class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = list()
        
        for i in range(len(operations) -1, -1, -1):
            stack.append(operations[i])

        scores = list()
        while stack:
            val = stack.pop()
            if val == "D":
                scores.append(2 * scores[-1])
            elif val == "C":
                scores.pop()
            elif val == "+":
                scores.append(scores[-1] + scores[-2])
            else:
                scores.append(int(val))

        return sum(scores)
        
        