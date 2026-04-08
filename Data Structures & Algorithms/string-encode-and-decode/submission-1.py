class Solution:

    DELIMITER_FIELD = "#"

    def encode(self, strs: List[str]) -> str:
        # abcd -> 4#abcd
        result = ""
        for word in strs:
            result += f"{len(word)}{self.DELIMITER_FIELD}{word}"
        print(result)
        return result

    def decode(self, s: str) -> List[str]:
        # 4#abcd -> abcd
        result = []

        i = 0
        while i < len(s):
            j = i
            while s[j] != self.DELIMITER_FIELD:
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            result.append(s[i:j])
            i = j
        return result