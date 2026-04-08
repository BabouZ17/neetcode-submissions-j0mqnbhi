class Solution:
    def isValid(self, s: str) -> bool:
        valid = {"(": ")", "{": "}", "[": "]"}
        stack = list()

        for c in s:
            if stack and c == valid.get(stack[-1]):
                stack.pop()
            else:
                stack.append(c)
        return True if len(stack) == 0 else False
            