from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        counts = defaultdict(list)

        for word in strs:
            chars = [0] * 26
            for c in word:
                chars[ord(c) - ord('a')] += 1
            counts[tuple(chars)].append(word)
        return counts.values()