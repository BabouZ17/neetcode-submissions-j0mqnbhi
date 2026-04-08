from string import ascii_lowercase
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:        
        res = list()
        while columnNumber > 0:
            columnNumber -= 1
            offset = columnNumber % 26
            res += chr(ord('A') + offset)
            columnNumber //= 26
        return "".join(reversed(res))

        return res.upper()