class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        cnt = Counter(words[0])

        for w in words:
            cur_cnt = Counter(w)
            for char in cnt:
                cnt[char] = min(cnt[char], cur_cnt[char])

        res = []
        for char in cnt:
            for i in range(cnt[char]):
                res.append(char)
        return res
        