class Solution:
    def isValid(self, s: str) -> bool:
        values = {"}": "{", "]": "[", ")": "("}
        stack = list()

        for char in s:
            if char in values:
                if stack and stack[-1] == values[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char) 
        return not stack
            