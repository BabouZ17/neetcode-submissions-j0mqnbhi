class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_hash = dict()

        for c in s:
            s_hash[c] = s_hash.get(c, 0) + 1
        
        for c in t:
            if c in s_hash:
                s_hash[c] -= 1 if s_hash[c] > 0 else 0
                if s_hash[c] == 0:
                    del s_hash[c]
            else:
                return False
        print(s_hash)
        return True if not s_hash else False