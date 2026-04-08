from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        for i in range(len(s2)):
            c = Counter(s1)
            while i < len(s2) and s2[i] in c:
                if c[s2[i]] > 1:
                    c[s2[i]] -= 1
                else:
                    del c[s2[i]]

                if not c:
                    return True
                i += 1
        return False
            