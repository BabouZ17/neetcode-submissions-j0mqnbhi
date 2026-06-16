from collections import Counter

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        letters = Counter(chars)
        res = 0

        for word in words:
            curr_cnt = Counter(word)
            if all(curr_cnt[c] <= letters[c] for c in curr_cnt):
                res += len(word)
        return res