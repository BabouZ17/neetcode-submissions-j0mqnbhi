from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for string in strs:
            freqs = [0] * 26
            for char in string:
                freqs[ord(char) - ord('a')] += 1
            res[tuple(freqs)].append(string)
        return list(res.values())