class Solution:
    def isValid(self, s: str) -> bool:
        parenthesis = {"]": "[", ")": "(", "}": "{"}

        stack = []

        for char in s:
            if char not in parenthesis:
                stack.append(char)
                continue
            
            if not stack or stack[-1] != parenthesis.get(char):
                return False
            stack.pop()
            
        return len(stack) == 0