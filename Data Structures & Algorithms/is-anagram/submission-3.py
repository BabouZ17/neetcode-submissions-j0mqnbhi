class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s_hash = dict()
        t_hash = dict()
        for i in range(len(s)):
            s_hash[s[i]] = s_hash.get(s[i], 0) + 1
            if len(t) > i:
                t_hash[t[i]] = t_hash.get(t[i], 0) + 1

        return s_hash == t_hash