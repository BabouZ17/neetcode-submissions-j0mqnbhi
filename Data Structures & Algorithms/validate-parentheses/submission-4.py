class Solution:
    def isValid(self, s: str) -> bool:
        parenthesis = {")": "(", "}": "{", "]":"["}

        stack = list()
        s_list = list(s)
        
        for i in range(len(s_list)):
            if s_list[i] not in parenthesis.keys():
                stack.append(s_list[i])
            else:
                last_value = stack[- 1] if len(stack) != 0 else "" # get last value
                if last_value == parenthesis[s_list[i]]:
                    stack = stack[:len(stack) - 1] # pop
                else:
                    return False
        return len(stack) == 0