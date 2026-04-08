class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_s = ""
        for char in s:
            if char.isalnum():
                cleaned_s += char.lower()
            
        L = len(cleaned_s)
        if L % 2 == 0:
            middle = int(L / 2)
            for i in range(middle):
                if cleaned_s[i] != cleaned_s[L-i-1]:
                    return False
        else:
            middle = int(((L-1) / 2))
            print(middle)        
            for i in range(1, middle+1):
                if cleaned_s[middle + i] != cleaned_s[middle - i]:
                    return False
        return True