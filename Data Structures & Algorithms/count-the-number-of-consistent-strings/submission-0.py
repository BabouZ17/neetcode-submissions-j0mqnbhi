class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed_letters = set(allowed)
        res = 0

        for word in words:
            if set(word).issubset(allowed_letters):
                res += 1
        return res