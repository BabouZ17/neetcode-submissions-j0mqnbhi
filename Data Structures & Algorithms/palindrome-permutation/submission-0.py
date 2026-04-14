from collections import defaultdict
class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        freqs = defaultdict(int)

        for char in s:
            freqs[char] += 1
        
        number_of_odd = 0
        for freq in freqs.values():
            if not (freq % 2 == 0):
                number_of_odd += 1
        return number_of_odd <= 1