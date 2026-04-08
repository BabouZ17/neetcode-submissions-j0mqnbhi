class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        res = list()
        count = 0

        for char in s:
            if char == "(":
                res.append(char)
                count += 1
            elif char == ")" and count > 0:
                res.append(char)
                count -= 1
            elif char != ")":
                res.append(char)

        filtered = list()
        for char in reversed(res):
            if char == "(" and count > 0:
                count -= 1
            else:
                filtered.append(char)

        return "".join(reversed(filtered))

