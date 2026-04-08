class Solution:
    def isValid(self, s: str) -> bool:
        parenthesis = {"]": "[", ")": "(", "}": "{"}

        stack = []

        for char in s:
            if stack and stack[-1] == parenthesis.get(char):
                stack.pop()
            else:
                stack.append(char)
            print(stack)
        return len(stack) == 0