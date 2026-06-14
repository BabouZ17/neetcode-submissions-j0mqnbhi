import string

class Solution:
    def customSortString(self, order: str, s: str) -> str:
        alphabet = string.ascii_lowercase
        mapping = {}

        i = 0
        for char in order:
            mapping[char] = i
            i += 1
        
        for char in alphabet:
            if char not in mapping:
                mapping[char] = i
                i += 1

        res = list(s)
        res.sort(key=lambda x: mapping[x])
        return "".join(res)