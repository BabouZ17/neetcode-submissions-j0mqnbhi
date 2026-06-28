class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        total = 0

        for operation in operations:

            if operation == "+":
                val = stack[-1] + stack[-2]
                stack.append(val)
                total += val
            elif operation == "D":
                val = 2*stack[-1]
                stack.append(val)
                total += val
            elif operation == "C":
                total -= stack.pop()
            else:
                val = int(operation)
                stack.append(val)
                total += val
                
        return total