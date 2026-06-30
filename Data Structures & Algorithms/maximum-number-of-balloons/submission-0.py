from collections import Counter
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        balloon = Counter("balloon")
        countText = Counter(text)

        res = len(text)
        for c in balloon:
            res = min(res, countText[c] // balloon[c])
        return res
