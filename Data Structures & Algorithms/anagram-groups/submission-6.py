from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for word in strs:
            curr_letters = [0] * 26
            for char in word:
                curr_letters[ord('a') - ord(char)] += 1
            res[tuple(curr_letters)].append(word)
        return list(res.values())
